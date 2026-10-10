from etl.cleaning import clean_amount

def test_plain_number():
    assert clean_amount("100") == 100.0

def test_commas_and_spaces():
    assert clean_amount(" 1,234.50 ") == 1234.50

def test_accounting_negative():
    assert clean_amount("(200)") == -200.0

def test_blank_is_zero():
    assert clean_amount("") == 0.0