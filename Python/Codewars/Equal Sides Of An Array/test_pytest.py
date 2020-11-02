import EqualSidesOfAnArray
    
def test_web():
    assert EqualSidesOfAnArray.find_even_index([1,2,3,4,3,2,1]) == 3
    assert EqualSidesOfAnArray.find_even_index([1,100,50,-51,1,1]) == 1
    assert EqualSidesOfAnArray.find_even_index([1,2,3,4,5,6]) == -1
    assert EqualSidesOfAnArray.find_even_index([20,10,30,10,10,15,35]) == 3
    assert EqualSidesOfAnArray.find_even_index([20,10,-80,10,10,15,35]) == 0
    assert EqualSidesOfAnArray.find_even_index([10,-80,10,10,15,35,20]) == 6
    assert EqualSidesOfAnArray.find_even_index(list(range(1,100))) == -1
    assert EqualSidesOfAnArray.find_even_index([0,0,0,0,0]) == 0
    assert EqualSidesOfAnArray.find_even_index([-1,-2,-3,-4,-3,-2,-1]) == 3
    assert EqualSidesOfAnArray.find_even_index(list(range(-100,-1))) == -1