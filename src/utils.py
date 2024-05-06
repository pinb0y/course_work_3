import json

from src.transaction import Transaction


def load_operations(path: str) -> list[dict]:
    """
    Загружает список операций из файла и конвертирует json в список
    :param path: путь к файлу с профессиями
    :return: список профессий
    """

    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_last_five_sorted_to_date_executed_operations(operations_list):
    executed_transactions = []

    for operation in operations_list:
        if operation.get("state") == "EXECUTED":
            executed_transactions.append(operation)

    executed_transactions.sort(key=lambda x: x['date'], reverse=True)

    return executed_transactions[:5]


def make_five_last_transaction_objects(operations_list):
    operation_objects = []
    for operation in operations_list:
        operation_objects.append(
            Transaction(operation['date'],
                        operation['operationAmount'], operation["description"],
                        operation.get("from"), operation["to"]))
    return operation_objects
