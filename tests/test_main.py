from src.main import show_some_last_operations
from tests.conftest import test_operation


def test_show_some_last_operations():
    assert show_some_last_operations([test_operation]) is None
