from tests.conftest import test_operation


def test_change_time_format():
    assert test_operation.change_time_format() == "23.11.2018"


def test_mask_number():
    assert test_operation.mask_number(test_operation.from_who) == "Visa Platinum 5355 13** **** 8236"
    assert test_operation.mask_number(test_operation.to_whom) == "Maestro 8045 76** **** 9061"


def test_str():
    assert test_operation.__str__() == ('23.11.2018 Перевод с карты на карту\n'
                                        'Visa Platinum 5355 13** **** 8236 -> Maestro 8045 76** **** 9061\n'
                                        '79428.73 USD')
