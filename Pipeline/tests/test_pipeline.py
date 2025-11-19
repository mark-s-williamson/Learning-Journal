from pipeline.transform import clean_salary, hash_password, clean_phone_number

def test_clean_salary():
    assert clean_salary("£27,000.00") == 27000.0
    assert clean_salary("£27,000.00 GBP") == 27000.0
    assert clean_salary("€5.000,00", period=12) == 60000.0
    assert clean_salary("-$50000.00") == 50000.0
    assert clean_salary(None) is None

def test_hash_password():
    hashed = hash_password("test123")
    assert isinstance(hashed, str)
    assert len(hashed) == 64  # SHA-256 hash length

def test_clean_phone_number():
    assert clean_phone_number("(123) 456-7890") == "1234567890"
    assert clean_phone_number("+1-800-555-0199") == "18005550199"
    assert clean_phone_number("0044 20 7946 0958") == "00442079460958"