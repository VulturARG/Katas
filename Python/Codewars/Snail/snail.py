def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = list(zip(*array))
        array.reverse()
    return a


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
#expected = [1,2,3,6,9,8,7,4,5]
array = [[1]]
print(snail(array))
