import seasons


def test_get_age_in_minutes():
    dob = '2000-01-01'
    expected_age = 10512000  # 20 years in minutes
    assert seasons.get_age_in_minutes(dob) == expected_age


def test_age_in_words():
    age = 10512000  # 20 years in minutes
    expected_age_words = '20 years'
    assert seasons.age_in_words(age) == expected_age_words

    age = 525600 + 43800 + 1440 + 5  # 1 year, 1 month, 1 day, 5 minutes
    expected_age_words = '1 year 1 month 1 day 5 minutes'
    assert seasons.age_in_words(age) == expected_age_words

    age = 1440 + 5  # 1 day, 5 minutes
    expected_age_words = '1 day 5 minutes'
    assert seasons.age_in_words(age) == expected_age_words

    age = 5  # 5 minutes
    expected_age_words = '5 minutes'
    assert seasons.age_in_words(age) == expected_age_words
