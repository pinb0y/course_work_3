class Transaction:
    """
    Класс транзакции.
    """

    def __init__(self, date: str, operation_amount: dict, description: str, from_who: str, to_whom: str) -> None:
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.from_who = from_who
        self.to_whom = to_whom

    def __str__(self) -> str:
        return (f"{self.change_time_format()} {self.description}\n"
                f"{self.mask_number(self.from_who)} -> {self.mask_number(self.to_whom)}\n"
                f"{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}")

    def change_time_format(self) -> str:
        """
        Переформатирует временной формат в ДД.ММ.ГГГГ
        :return:
        """
        year, month, date = self.date.split('-')
        return f"{date[:2]}.{month}.{year}"

    def mask_number(self, value: str) -> str:
        """
        Маскирует цифры в номере карты или счета
        :param value: номер карты откуда или куда
        :return: номер карты или счета в замаскированном виде
        """
        if self.description == "Открытие вклада" and value == self.from_who:
            return ""

        value_list: list = value.split()
        number: str = ''
        text: list = []

        for value in value_list:
            if value.isalpha():
                text.append(value)
            else:
                number = value

        text: str = ' '.join(text)

        if text == 'Счет':
            cut_number: str = number[-4:]
            masked_bill_number: str = '**' + cut_number
            return f'{text} {masked_bill_number}'
        else:
            masked_card_number: str = number[:6] + "******" + number[-4:]
            masked_card_number_with_spaces: str = masked_card_number[
                                             :4] + " " + masked_card_number[
                                                         4:8] + " " + masked_card_number[
                                                                      8:12] + " " + masked_card_number[
                                                                                    12:]

            return f'{text} {masked_card_number_with_spaces}'
