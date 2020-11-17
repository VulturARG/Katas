import more_populate_year
    
def test_web():
    assert more_populate_year.search_year([[2000,2010],[1984,2003],[1987,2002]]) == [2000,3]
    
    arr =  [[2000,2010],[1975,2005],[1975,2003],[1803,1849],[1750,1869],[1840,1935],[1803,1921],[1894,1921]]
    assert more_populate_year.search_year(arr) == [1840,4]