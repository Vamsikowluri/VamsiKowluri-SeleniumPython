import pytest


def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("Good morning")
