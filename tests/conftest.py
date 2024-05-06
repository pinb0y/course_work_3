from src.transaction import Transaction

operation = {
    "id": 34148726,
    "state": "EXECUTED",
    "date": "2018-11-23T23:52:36.999661",
    "operationAmount": {
        "amount": "79428.73",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Platinum 5355133159258236",
    "to": "Maestro 8045769817179061"
}

test_operation = Transaction(operation['date'],
                             operation['operationAmount'],
                             operation["description"],
                             operation.get("from"),
                             operation["to"])