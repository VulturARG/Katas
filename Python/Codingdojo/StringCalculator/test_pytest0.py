import stringCalculator
    
def test_empty_string_equal_zero():
    assert stringCalculator.add("") == "0"
def test_one_number_in_string_return_same_string():
    assert stringCalculator.add("1") == "1"
def test_two_numbers_sepparated_by_comma_return_number_one_plus_number_two():
    assert stringCalculator.add("1.1,2.2") == "3.3"
def test_many_numbers():
    assert stringCalculator.add("1,2,3,4,5") == "15"
def test_new_line_as_separator():
    assert stringCalculator.add("1\n2,3") == "6"
    assert stringCalculator.add("175.2,\n35") == "Number expected but '\n' found at position 6."
    assert stringCalculator.add("10,175.2,\n35") == "Number expected but '\n' found at position 9."
    assert stringCalculator.add("10\n175.2,\n35") == "Number expected but '\n' found at position 9."
def test_Missing_number_in_last_position():
    assert stringCalculator.add("1,3,") == "Number expected but EOF found."
def test_Custom_separators():
    assert stringCalculator.add("//;\n1;2") == "3"
    assert stringCalculator.add("//|\n1|2|3") == "6"
    assert stringCalculator.add("//sep\n2sep3") == "5"
    assert stringCalculator.add("//|\n1|2,3") == "'|' expected but ',' found at position 3."
def test_Negative_numbres():
    assert stringCalculator.add("-1,2") == "Negative not allowed : -1"
    assert stringCalculator.add("2,-4,-5") == "Negative not allowed : -4, -5"