from bank import value


def test_value():
    assert value("hello world") == 0
    assert value("Hello, how are you?") == 0
    assert value("hi there") == 20
    assert value("hey") == 20
    assert value("goodbye") == 100
    assert value("123") == 100
    assert value("") == 100
    assert value("H") == 20
