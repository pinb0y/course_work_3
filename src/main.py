from src.settings import TRANSACTIONS_PATH
from src.utils import make_five_last_transaction_objects, get_last_five_sorted_to_date_executed_operations, \
    load_operations

five_last_operations = make_five_last_transaction_objects(
    get_last_five_sorted_to_date_executed_operations(load_operations(TRANSACTIONS_PATH)))


def show_five_last_operations(operations):
    for operation in operations:
        print(operation, end='\n\n')


if __name__ == "__main__":
    show_five_last_operations(five_last_operations)
