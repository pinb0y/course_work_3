from src.utils import get_last_some_sorted_to_date_executed_operations, make_some_last_transaction_objects


def test_load_operations():
    ...


def test_get_last_some_sorted_to_date_executed_operations():
    assert get_last_some_sorted_to_date_executed_operations([
        {"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230"},
        {"state": "EXECUTED", "date": "2018-08-19T04:27:37.904916"},
        {"state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"state": "EXECUTED", "date": "2018-01-26T15:40:13.413061"},
        {"state": "EXECUTED", "date": "2018-11-29T07:18:23.941293"},
        {"state": "EXECUTED", "date": "2018-10-14T22:27:25.205631"},
        {"state": "CANCELED", "date": "2018-11-23T17:47:33.127140"}
    ], 3) == [
               {"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230"},
               {"state": "EXECUTED", "date": "2018-11-29T07:18:23.941293"},
               {"state": "EXECUTED", "date": "2018-10-14T22:27:25.205631"},
           ]

    assert get_last_some_sorted_to_date_executed_operations([
        {"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230"},
        {"state": "EXECUTED", "date": "2018-08-19T04:27:37.904916"},
        {"state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"state": "EXECUTED", "date": "2018-01-26T15:40:13.413061"},
        {"state": "EXECUTED", "date": "2018-11-29T07:18:23.941293"},
        {"state": "EXECUTED", "date": "2018-10-14T22:27:25.205631"},
        {"state": "CANCELED", "date": "2018-11-23T17:47:33.127140"}
    ], 0) == []

    assert get_last_some_sorted_to_date_executed_operations([
        {"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230"},
        {"state": "EXECUTED", "date": "2018-08-19T04:27:37.904916"},
        {"state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"state": "EXECUTED", "date": "2018-01-26T15:40:13.413061"},
        {"state": "EXECUTED", "date": "2018-11-29T07:18:23.941293"},
        {"state": "EXECUTED", "date": "2018-10-14T22:27:25.205631"},
        {"state": "CANCELED", "date": "2018-11-23T17:47:33.127140"}
    ], 6) == [
               {"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230"},
               {"state": "EXECUTED", "date": "2018-11-29T07:18:23.941293"},
               {"state": "EXECUTED", "date": "2018-10-14T22:27:25.205631"},
               {"state": "EXECUTED", "date": "2018-08-19T04:27:37.904916"},
               {"state": "EXECUTED", "date": "2018-01-26T15:40:13.413061"},
           ]

    assert get_last_some_sorted_to_date_executed_operations([
        {"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230"},
        {"state": "EXECUTED", "date": "2018-08-19T04:27:37.904916"},
        {"state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"state": "CANCELED", "date": "2018-01-26T15:40:13.413061"},
        {"state": "CANCELED", "date": "2018-11-29T07:18:23.941293"},
        {"state": "CANCELED", "date": "2018-10-14T22:27:25.205631"},
        {"state": "CANCELED", "date": "2018-11-23T17:47:33.127140"}
    ], 4) == [
               {"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230"},
               {"state": "EXECUTED", "date": "2018-08-19T04:27:37.904916"},
           ]

    assert get_last_some_sorted_to_date_executed_operations([
        {"state": "CANCELED", "date": "2019-07-12T20:41:47.882230"},
        {"state": "CANCELED", "date": "2018-08-19T04:27:37.904916"},
        {"state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"state": "CANCELED", "date": "2018-01-26T15:40:13.413061"},
        {"state": "CANCELED", "date": "2018-11-29T07:18:23.941293"},
        {"state": "CANCELED", "date": "2018-10-14T22:27:25.205631"},
        {"state": "CANCELED", "date": "2018-11-23T17:47:33.127140"}
    ], 4) == []

