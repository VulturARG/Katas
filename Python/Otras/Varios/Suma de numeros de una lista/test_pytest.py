import sum
    
def test_web():
    assert sum.sum_search([10, 15, 3, 7],17) == True
    assert sum.sum_search([10, 15, 3, 7],12) == False
    
    assert sum.sum_search_google([1, 2, 3, 9],8) == False
    assert sum.sum_search_google([1, 2, 4, 4],8) == True
    
    assert sum.order_first([10, 15, 3, 7],17) == True
    assert sum.order_first([10, 15, 3, 7],12) == False
    
    assert sum.sum_search_google_no_order([1, 2, 3, 9],8) == False
    assert sum.sum_search_google_no_order([1, 2, 4, 4],8) == True
    assert sum.sum_search_google_no_order([4, 2, 1, 4],8) == True
    