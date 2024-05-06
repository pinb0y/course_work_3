from src.settings import TRANSACTIONS_PATH, TRANSACTIONS_QUANTITY
from src.transaction import Transaction
from src.utils import make_some_last_transaction_objects, get_last_some_sorted_to_date_executed_operations, \
    load_operations

some_last_operations = make_some_last_transaction_objects(
    get_last_some_sorted_to_date_executed_operations(load_operations(TRANSACTIONS_PATH), TRANSACTIONS_QUANTITY))


def show_some_last_operations(operations: list[Transaction]) -> None:
    """
    Показывает заданное количество последних операций в формате
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    :param operations: список экземпляров класса Transaction
    :return: None
    """
    for operation in operations:
        print(operation, end='\n\n')


if __name__ == "__main__":
    show_some_last_operations(some_last_operations)
