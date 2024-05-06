from pathlib import Path

# Корневой путь
ROOT_PATH = Path(__file__).parent.parent
# путь к папке дата
DATA_PATH = ROOT_PATH.joinpath('data')
# путь к файлу с транзакциями
TRANSACTIONS_PATH = DATA_PATH.joinpath('operations.json')

# количество выводимых операций
TRANSACTIONS_QUANTITY = 5
