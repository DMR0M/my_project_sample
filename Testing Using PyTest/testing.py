"""Writing Sample First Test Suite Using PyTest"""

ANSWER: int = 15


def test_login():
    print('Login Successful')


def test_logoff():
    print('Logoff Successful')


def test_calculation():
    assert 10+3 == ANSWER
