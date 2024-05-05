class Transaction:
    def __init__(self, operation_id, date: str, state, operation_amount, description, from_who: str, to_whom):
        self.operation_id = operation_id
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_who = from_who
        self.to_whom = to_whom

    def change_time_format(self):
        year, month, date = self.date.split('-')
        return f"{date[:2]}.{month}.{year}"

    def mask_from_who(self):
        text, number = self.from_who.split()
        if text == 'Счет':
            cut_number = number[-4:]
            masked_bill_number = '**' + cut_number
            return f' {text} {masked_bill_number}'
        else:
            masked_card_number = number[:6] + "******" + number[-4:]
            masked_card_number_with_spaces = masked_card_number[
                                             :4] + " " + masked_card_number[
                                                         4:8] + " " + masked_card_number[
                                                                      8:12] + " " + masked_card_number[
                                                                                    12:]
            return f'{text} {masked_card_number_with_spaces}'

    def mask_to_whom(self):
        text, number = self.to_whom.split()
        if text == 'Счет':
            cut_number = number[-4:]
            masked_bill_number = '**' + cut_number
            return f' {text} {masked_bill_number}'
        else:
            masked_card_number = number[:6] + "******" + number[-4:]
            masked_card_number_with_spaces = masked_card_number[
                                             :4] + " " + masked_card_number[
                                                         4:8] + " " + masked_card_number[
                                                                      8:12] + " " + masked_card_number[
                                                                                    12:]
            return f'{text} {masked_card_number_with_spaces}'
