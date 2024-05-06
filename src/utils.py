import json

from src.settings import TRANSACTIONS_PATH
from src.transaction import Transaction


def load_operations(path: str) -> list[dict]:
    """
    Загружает список транзакций из файла и конвертирует json в список
    :param path: путь к файлу с профессиями
    :return: список профессий
    """

    with open(path, encoding='utf-8') as file:
        return json.load(file)


def sort_to_date_operations(operations_list):
    executed_transactions = []

    for operation in operations_list:
        if operation.get("state") == "EXECUTED":
            executed_transactions.append(operation)

    executed_transactions.sort(key=lambda x: x['date'], reverse=True)

    return executed_transactions[:5]


def get_five_last_operations(operations_list):
    operation_objects = []
    for operation in operations_list:
        operation_objects.append(
            Transaction(operation['id'], operation['state'], operation['date'],
                        operation['operationAmount'], operation["description"],
                        operation.get("from"), operation["to"]))
    return operation_objects


result = get_five_last_operations(sort_to_date_operations(load_operations(TRANSACTIONS_PATH)))
for i in result:
    print(i)
    print()
