class Transaction:
    def __init__(self, date, operation_amount, description, from_who, to_whom):
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.from_who = from_who
        self.to_whom = to_whom

    def __str__(self):
        return (f"{self.change_time_format()} {self.description}\n"
                f"{self.mask_number(self.from_who)} -> {self.mask_number(self.to_whom)}\n"
                f"{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}")

    def change_time_format(self):
        year, month, date = self.date.split('-')
        return f"{date[:2]}.{month}.{year}"

    def mask_number(self, value):
        if self.description == "Открытие вклада" and value == self.from_who:
            return ""
        value_list = value.split()
        number = ''
        text = []
        for value in value_list:
            if value.isalpha():
                text.append(value)
            else:
                number = value
        text = ' '.join(text)
        if text == 'Счет':
            cut_number = number[-4:]
            masked_bill_number = '**' + cut_number
            return f'{text} {masked_bill_number}'
        else:
            masked_card_number = number[:6] + "******" + number[-4:]
            masked_card_number_with_spaces = masked_card_number[
                                             :4] + " " + masked_card_number[
                                                         4:8] + " " + masked_card_number[
                                                                      8:12] + " " + masked_card_number[
                                                                                    12:]
            return f'{text} {masked_card_number_with_spaces}'
