# tests/test_main.py
from lds_coding_task.main import hello


def test_hello() -> None:
    assert hello() == "Hello from lds-coding-task"
