from um import count


def test_count_zero_occurrences():
    assert count("hello, world") == 0


def test_count_one_occurrence():
    assert count("um, excuse me") == 1


def test_count_multiple_occurrences():
    assert count("um, well, um, you know") == 2


def test_count_case_insensitive():
    assert count("Um, um, uM") == 3


def test_count_no_input():
    assert count("") == 0
