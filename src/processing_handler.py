import boto3
import json
import logging
from botocore.exceptions import ClientError
from src.utils.dim_currency import get_currency_data
from src.utils.dim_counterparty import dim_counter_party
from src.utils.dim_date import dim_date
from src.utils.dim_design import make_new_design_table
from src.utils.dim_location import to_dim_location
from src.utils.dim_staff import create_dim_staff
from src.utils.fact_sales import fact_sales_util
from src.utils.parquet_converter import parquet_converter

logger = logging.getLogger('TransformLogger')
#Not sure if we want to use same logger as ingestion function here - they're going to be going to different log groups.
logger.setLevel(logging.INFO)


def processing_handler(event, context):
    '''
    This finds the latest file in the s3 bucket, gets it from the bucket, and runs transformation functions on it.
    '''
    try:
        utils_dict = {
            'currency': get_currency_data,
            'counterparty': dim_counter_party,
            'date': dim_date,
            'design': make_new_design_table,
            'location': to_dim_location,
            'staff': create_dim_staff,
            'sales_order': fact_sales_util,
        }
        json_data = get_latest_file(event)
        #Once the json data has been accessed, it is split up for use by other functions.
        processed_data = []
        processed_table_names = []
        for key, value in json_data.items():
            for data in value:
                if data == []:
                    continue
                else:
                    processed_data.append(utils_dict[key](json_data))
                    processed_table_names.append(key)
        
        parquet_converter(processed_data, processed_table_names)

        event_names_for_erros = get_object_path(event)
        s3_object_name = event_names_for_erros['object']
    
    except KeyError:
        logger.error('There was an issue with the bucket data, please investigate.')
    except ClientError as c:
        if c.response['Error']['Code'] == 'NoSuchKey':
            logger.error(f'No object found - {s3_object_name}')
        elif c.response['Error']['Code'] == 'NoSuchBucket':
            logger.error(f'Processed data bucket is missing')
        else:
            raise
    except InvalidFileTypeError:
        logger.error(f'File {s3_object_name} is not a JSON')
    except Exception as e:
        logger.error(e)
        raise RuntimeError



def get_latest_file(event):
    '''This is run within the handler to retrieve the object that triggered the most recent event.'''
    try:    
        event_names = get_object_path(event)
        s3_bucket_name = event_names['bucket']
        s3_object_name = event_names['object']
        logger.info(f'Bucket is {s3_bucket_name}')
        logger.info(f'Object is {s3_object_name}')

        if s3_object_name[-4:] != 'json':
            raise InvalidFileTypeError
        s3 = boto3.client('s3')

        #From my reading, the following code block, which finds the last-modified object in the bucket, is
        #redundant with the above code, which finds the name of the object that triggered the current eventbridge event
        #which should always be the most recent object.

        # response = s3.list_objects_v2(Bucket=s3_bucket_name)['Contents']
        # last_modified = lambda response: int(response['LastModified'].strftime('%s'))
        # latest_file = [response['Key'] for response in sorted(response, key=last_modified, reverse=True)][0]

        get_data = s3.get_object(Bucket=s3_bucket_name, Key=s3_object_name)
        json_data = json.load(get_data['Body'])
        return json_data
    except ClientError as c:
        if c.response['Error']['Code'] == 'NoSuchKey':
            logger.error(f'No object found - {s3_object_name}')
        elif c.response['Error']['Code'] == 'NoSuchBucket':
            logger.error(f'No such bucket - {s3_bucket_name}')
        else:
            raise
    except InvalidFileTypeError:
        logger.error(f'File {s3_object_name} is not a JSON')
    except Exception as e:
        logger.error(e)
        raise RuntimeError




# def get_table_from_dict(latest_data, choice):
#     '''This takes two arguments, representing the return from get_latest_file and the chosen table name respectively, and extracts the data for the table matching choice. It returns table data.'''
#     try:
#         return latest_data[choice]
#     except KeyError:
#         print('You entered an invalid table name')

def get_object_path(event_file):
    """Extracts bucket and object references from Records field of event."""
    return {'bucket': event_file['Records'][0]['s3']['bucket']['name'],\
         'object': event_file['Records'][0]['s3']['object']['key']}

class InvalidFileTypeError(Exception):
    '''Handles errors where file is not a json'''