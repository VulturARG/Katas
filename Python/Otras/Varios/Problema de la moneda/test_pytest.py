import coins
    
def test_web():
    assert coins.change_greedy([5,10,25,50],126) == [[50, 2], [25, 1], [1, -1]]
    assert coins.change_greedy([1,5,10,25,50],127) == [[50, 2], [25, 1], [1, 2]]
    assert coins.change_greedy([],127) == [[127, -1]]
    