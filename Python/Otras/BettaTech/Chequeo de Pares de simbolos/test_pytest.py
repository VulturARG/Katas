import checkSymbol
    
def test_web():
    assert checkSymbol.check_symbol_open_close("[()]{}{[()()]()}") == True
    assert checkSymbol.check_symbol_open_close("[([])]{}{[()()]()}") == True
    assert checkSymbol.check_symbol_open_close("[([()])]{}{[()()]()}") == True
    assert checkSymbol.check_symbol_open_close("[(])") == False
    assert checkSymbol.check_symbol_open_close("[([]])") == False
    assert checkSymbol.check_symbol_open_close("[([])") == False
    
    assert checkSymbol.scan("[()]{}{[()()]()}") == True
    assert checkSymbol.scan("[([])]{}{[()()]()}") == True
    assert checkSymbol.scan("[([()])]{}{[()()]()}") == True
    assert checkSymbol.scan("[(])") == False
    assert checkSymbol.scan("[([]])") == False
    assert checkSymbol.scan("[([])") == False
    