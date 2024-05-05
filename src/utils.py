import json

from src.transaction import Transaction


def load_operations(path: str) -> list[dict]:
    """
    Загружает список транзакций из файла и конвертирует json в список
    :param path: путь к файлу с профессиями
    :return: список профессий
    """

    with open(path, encoding='utf-8') as file:
        return json.load(file)


def make_5_last_operations(file):
    for i in range(len(file)):
        if file[i]["state"] == "EXECUTED":
            ...
