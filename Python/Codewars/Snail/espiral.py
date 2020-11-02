def snail(snail_map):
    n =  len(snail_map)
    for i in range(0,n):
        if i%2 ==0:
            for j in range(0,n):
                print(snail_map[j][i])
        else:
            for j in range(n-1,-1,-1):
                print(snail_map[j][i])




array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
#expected = [1,2,3,6,9,8,7,4,5]
print(snail(array))