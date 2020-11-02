import checkBracket
    
def test_web():
    assert checkBracket.check_symbol_open_close("[()]{}{[()()]()}") == True
    assert checkBracket.check_symbol_open_close("[([])]{}{[()()]()}") == True
    assert checkBracket.check_symbol_open_close("[([()])]{}{[()()]()}") == True
    assert checkBracket.check_symbol_open_close("[(])") == False
    assert checkBracket.check_symbol_open_close("[([]])") == False
    assert checkBracket.check_symbol_open_close("[([])") == False
    