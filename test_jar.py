from jar import Jar


def test_init():
    j = Jar(10)
    assert j.capacity == 10
    assert j.size == 0

    j = Jar()
    assert j.capacity == 12
    assert j.size == 0

    try:
        j = Jar(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected a ValueError."


def test_deposit():
    j = Jar(5)
    j.deposit(2)
    assert j.size == 2

    j.deposit(3)
    assert j.size == 5

    try:
        j.deposit(1)
    except ValueError:
        pass
    else:
        assert False, "Expected a ValueError."


def test_withdraw():
    j = Jar(5)
    j.deposit(3)
    j.withdraw(1)
    assert j.size == 2

    try:
        j.withdraw(3)
    except ValueError:
        pass
    else:
        assert False, "Expected a ValueError."


def test_str():
    j = Jar(3)
    assert str(j) == ""

    j.deposit(2)
    assert str(j) == "🍪🍪"

    j.withdraw(1)
    assert str(j) == "🍪"


def test_capacity():
    j = Jar(5)
    assert j.capacity == 5

    j = Jar()
    assert j.capacity == 12


def test_size():
    j = Jar(5)
    assert j.size == 0

    j.deposit(2)
    assert j.size == 2

    j.withdraw(1)
    assert j.size == 1
