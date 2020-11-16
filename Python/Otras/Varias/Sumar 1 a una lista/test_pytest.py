import plus_one_to_list
    
def test_web():
    assert plus_one_to_list.plus_one([1,3,4]) == [1,3,5]
    assert plus_one_to_list.plus_one([1,9,9]) == [2,0,0]
    assert plus_one_to_list.plus_one([9,9,9]) == [1,0,0,0]
    assert plus_one_to_list.plus_one([1,2,9]) == [1,3,0]
    assert plus_one_to_list.plus_one([1,2,9,9]) == [1,3,0,0]
    
    