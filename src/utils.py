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


def get_last_some_sorted_to_date_executed_operations(operations_list: list[dict],
                                                     operation_quantity: int) -> list[dict]:
    """
    Отбирает успешные операции, сортирует их по дате от ближайшей до дальней и выводит сколько надо последних.
    :param operation_quantity: Количество выводимых операций
    :param operations_list: Список с операциями клиента
    :return: список последними операциями
    """
    executed_transactions: list[dict] = []

    for operation in operations_list:
        if operation.get("state") == "EXECUTED":
            executed_transactions.append(operation)

    executed_transactions.sort(key=lambda x: x['date'], reverse=True)

    return executed_transactions[:operation_quantity]


def make_some_last_transaction_objects(operations_list: list[dict]) -> list[Transaction]:
    """
    Преобразует операции в экземпляры класса Transaction.
    :param operations_list: Список с последними операциями
    :return:
    """
    operation_objects: list[Transaction] = []
    for operation in operations_list:
        operation_objects.append(
            Transaction(operation['date'],
                        operation['operationAmount'], operation["description"],
                        operation.get("from"), operation["to"]))
    return operation_objects
