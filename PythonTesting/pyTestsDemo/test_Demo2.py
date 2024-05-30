import pytest

@pytest.mark.skip
def test_firstProgram():
    msg = 'Hello'
    assert msg == 'Hi', 'Test has been failed'


@pytest.mark.smoke
def test_secondCreditCard():
    a = 2
    b = 4
    c = a+b
    assert c == 6, 'Total is wrong'
