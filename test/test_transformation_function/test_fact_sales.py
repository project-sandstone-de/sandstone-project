"""Tests for fact_sales_util function"""
from processing import to_fact_sales


def test_fact_sales_util_returns_correct_keys_when_theres_data_passed():
    """Tests that fact_sales_util() returns all correct keys when there is data
    passed.
    """
    data = {"sales_order": {
        "sales_order_id": [1],
        "created_at": [],
        "last_updated": [],
        "design_id": [],
        "staff_id": [],
        "counterparty_id": [],
        "units_sold": [],
        "unit_price": [],
        "currency_id": [],
        "agreed_delivery_date": [],
        "agreed_payment_date": [],
        "agreed_delivery_location_id": []
    }, "test": "test"}

    result = to_fact_sales(data)

    expected_keys = ['sales_order_id', 'created_date', 'created_time',
                     'last_updated_date', 'last_updated_time',
                     'sales_staff_id', 'counterparty_id', 'units_sold',
                     'unit_price', 'currency_id', 'design_id',
                     'agreed_payment_date', 'agreed_delivery_date',
                     'agreed_delivery_location_id']

    print(list(result.keys()))

    assert list(result.keys()) == expected_keys


def test_fact_sales_util_returns_correct_date_and_times():
    """Tests that fact_sales_util() returns the correct date for each column'.
    """
    data = {"sales_order": {
        "sales_order_id": [
            1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 19, 21, 22, 18,
            25
        ],
        "created_at": [
            "2022-11-03 14:20:52.186000",
            "2022-11-03 14:20:52.186000",
            "2022-11-03 14:20:52.188000",
            "2022-11-03 14:20:52.188000",
            "2022-11-03 14:20:52.186000",
            "2022-11-04 11:37:10.341000",
            "2022-11-04 12:57:09.926000",
            "2022-11-04 13:45:10.306000",
            "2022-11-07 09:07:10.485000",
            "2022-11-07 15:53:10.153000",
            "2022-11-09 10:20:09.912000",
            "2022-11-09 15:16:10.492000",
            "2022-11-10 13:18:09.926000",
            "2022-11-11 08:51:10.286000",
            "2022-11-15 08:46:09.873000",
            "2022-11-16 09:05:10.336000",
            "2022-11-17 11:47:09.942000",
            "2022-11-17 17:13:10.235000",
            "2022-11-16 08:17:10.016000",
            "2022-11-18 12:27:09.924000"
        ],
        "last_updated": [
            "2022-11-03 14:20:52.186000",
            "2022-11-03 14:20:52.186000",
            "2022-11-03 14:20:52.188000",
            "2022-11-03 14:20:52.188000",
            "2022-11-03 14:20:52.186000",
            "2022-11-04 11:37:10.341000",
            "2022-11-04 12:57:09.926000",
            "2022-11-04 13:45:10.306000",
            "2022-11-07 09:07:10.485000",
            "2022-11-07 15:53:10.153000",
            "2022-11-09 10:20:09.912000",
            "2022-11-09 15:16:10.492000",
            "2022-11-10 13:18:09.926000",
            "2022-11-11 08:51:10.286000",
            "2022-11-15 08:46:09.873000",
            "2022-11-16 09:05:10.336000",
            "2022-11-17 11:47:09.942000",
            "2022-11-17 17:13:10.235000",
            "2022-11-16 08:17:10.016000",
            "2022-11-18 12:27:09.924000"
        ],
        "design_id": [
            9, 3, 4, 4, 7, 3, 7, 2, 3, 9, 2, 7, 6, 9, 7, 13, 5, 4, 56, 4
        ],
        "staff_id": [
            16, 19, 10, 10, 18, 13, 11, 11, 16, 14, 8, 3, 11, 7, 20, 13, 18, 7,
            20, 16
        ],
        "counterparty_id": [
            18, 8, 4, 16, 4, 18, 10, 20, 12, 12, 12, 7, 5, 10, 13, 10, 18, 11,
            17, 15
        ],
        "units_sold": [
            84754, 42972, 65839, 32069, 49659, 83908, 65453, 20381, 61620,
            35227, 7693, 2845, 82159, 74957, 36220, 41878, 42135, 92468, 93380,
            19231
        ],
        "unit_price": [
            "2.43",
            "3.94",
            "2.91",
            "3.89",
            "2.41",
            "3.99",
            "2.89",
            "2.22",
            "3.86",
            "3.41",
            "3.88",
            "2.97",
            "2.65",
            "3.25",
            "2.00",
            "2.29",
            "3.63",
            "2.70",
            "2.95",
            "2.45"
        ],
        "currency_id": [
            3, 2, 3, 2, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 3, 2, 2, 2
        ],
        "agreed_delivery_date": [
            "2022-11-10",
            "2022-11-07",
            "2022-11-06",
            "2022-11-05",
            "2022-11-05",
            "2022-11-04",
            "2022-11-04",
            "2022-11-06",
            "2022-11-09",
            "2022-11-08",
            "2022-11-13",
            "2022-11-16",
            "2022-11-15",
            "2022-11-12",
            "2022-11-20",
            "2022-11-17",
            "2022-11-18",
            "2022-11-20",
            "2022-11-20",
            "2022-11-22"
        ],
        "agreed_payment_date": [
            "2022-11-03",
            "2022-11-08",
            "2022-11-07",
            "2022-11-07",
            "2022-11-08",
            "2022-11-07",
            "2022-11-09",
            "2022-11-07",
            "2022-11-10",
            "2022-11-13",
            "2022-11-11",
            "2022-11-14",
            "2022-11-14",
            "2022-11-15",
            "2022-11-19",
            "2022-11-18",
            "2022-11-18",
            "2022-11-20",
            "2022-11-20",
            "2022-11-20"
        ],
        "agreed_delivery_location_id": [
            4, 8, 19, 15, 25, 17, 28, 8, 20, 13, 15, 2, 6, 28, 9, 15, 27, 19,
            2, 12
        ]
    }, "test": "test"}

    result = to_fact_sales(data)
    expected = {
        "created_time": [
            "14:20:52.186000",
            "14:20:52.186000",
            "14:20:52.188000",
            "14:20:52.188000",
            "14:20:52.186000",
            "11:37:10.341000",
            "12:57:09.926000",
            "13:45:10.306000",
            "09:07:10.485000",
            "15:53:10.153000",
            "10:20:09.912000",
            "15:16:10.492000",
            "13:18:09.926000",
            "08:51:10.286000",
            "08:46:09.873000",
            "09:05:10.336000",
            "11:47:09.942000",
            "17:13:10.235000",
            "08:17:10.016000",
            "12:27:09.924000"
        ],
        "created_date": [
            "2022-11-03",
            "2022-11-03",
            "2022-11-03",
            "2022-11-03",
            "2022-11-03",
            "2022-11-04",
            "2022-11-04",
            "2022-11-04",
            "2022-11-07",
            "2022-11-07",
            "2022-11-09",
            "2022-11-09",
            "2022-11-10",
            "2022-11-11",
            "2022-11-15",
            "2022-11-16",
            "2022-11-17",
            "2022-11-17",
            "2022-11-16",
            "2022-11-18"
        ],
        "last_updated_time": [
            "14:20:52.186000",
            "14:20:52.186000",
            "14:20:52.188000",
            "14:20:52.188000",
            "14:20:52.186000",
            "11:37:10.341000",
            "12:57:09.926000",
            "13:45:10.306000",
            "09:07:10.485000",
            "15:53:10.153000",
            "10:20:09.912000",
            "15:16:10.492000",
            "13:18:09.926000",
            "08:51:10.286000",
            "08:46:09.873000",
            "09:05:10.336000",
            "11:47:09.942000",
            "17:13:10.235000",
            "08:17:10.016000",
            "12:27:09.924000"
        ],
        "last_updated_date": [
            "2022-11-03",
            "2022-11-03",
            "2022-11-03",
            "2022-11-03",
            "2022-11-03",
            "2022-11-04",
            "2022-11-04",
            "2022-11-04",
            "2022-11-07",
            "2022-11-07",
            "2022-11-09",
            "2022-11-09",
            "2022-11-10",
            "2022-11-11",
            "2022-11-15",
            "2022-11-16",
            "2022-11-17",
            "2022-11-17",
            "2022-11-16",
            "2022-11-18"
        ],
        "sales_order_id": [
            1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 19, 21, 22, 18,
            25
        ],
        "design_id": [9, 3, 4, 4, 7, 3, 7, 2, 3, 9, 2, 7, 6, 9, 7, 13, 5, 4,
                      56, 4],
        "sales_staff_id": [
            16, 19, 10, 10, 18, 13, 11, 11, 16, 14, 8, 3, 11, 7, 20, 13, 18, 7,
            20,
            16
        ],
        "counterparty_id": [
            18, 8, 4, 16, 4, 18, 10, 20, 12, 12, 12, 7, 5, 10, 13, 10, 18, 11,
            17, 15
        ],
        "units_sold": [
            84754, 42972, 65839, 32069, 49659, 83908, 65453, 20381, 61620,
            35227, 7693, 2845, 82159, 74957, 36220, 41878, 42135, 92468, 93380,
            19231
        ],
        "unit_price": [
            "2.43",
            "3.94",
            "2.91",
            "3.89",
            "2.41",
            "3.99",
            "2.89",
            "2.22",
            "3.86",
            "3.41",
            "3.88",
            "2.97",
            "2.65",
            "3.25",
            "2.00",
            "2.29",
            "3.63",
            "2.70",
            "2.95",
            "2.45"
        ],
        "currency_id": [3, 2, 3, 2, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 3, 2,
                        2, 2
                        ],
        "agreed_delivery_date": [
            "2022-11-10",
            "2022-11-07",
            "2022-11-06",
            "2022-11-05",
            "2022-11-05",
            "2022-11-04",
            "2022-11-04",
            "2022-11-06",
            "2022-11-09",
            "2022-11-08",
            "2022-11-13",
            "2022-11-16",
            "2022-11-15",
            "2022-11-12",
            "2022-11-20",
            "2022-11-17",
            "2022-11-18",
            "2022-11-20",
            "2022-11-20",
            "2022-11-22"
        ],
        "agreed_payment_date": [
            "2022-11-03",
            "2022-11-08",
            "2022-11-07",
            "2022-11-07",
            "2022-11-08",
            "2022-11-07",
            "2022-11-09",
            "2022-11-07",
            "2022-11-10",
            "2022-11-13",
            "2022-11-11",
            "2022-11-14",
            "2022-11-14",
            "2022-11-15",
            "2022-11-19",
            "2022-11-18",
            "2022-11-18",
            "2022-11-20",
            "2022-11-20",
            "2022-11-20"
        ],
        "agreed_delivery_location_id": [
            4, 8, 19, 15, 25, 17, 28, 8, 20, 13, 15, 2, 6, 28, 9, 15, 27, 19,
            2, 12
        ]
    }

    assert result == expected
