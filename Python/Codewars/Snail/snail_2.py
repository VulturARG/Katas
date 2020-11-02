def snail(snail_map):
    if snail_map == [[]]: return []
    fileMax = len(snail_map)
    snail_list = []
    lowerLimit = 0
    upperLimit = fileMax
    for j in range(fileMax):
        [snail_list.append(snail_map[lowerLimit][i])   for i in range(lowerLimit,upperLimit)]
        [snail_list.append(snail_map[i][upperLimit-1]) for i in range(lowerLimit+1,upperLimit)]
        [snail_list.append(snail_map[upperLimit-1][i]) for i in range(upperLimit-2,lowerLimit-1,-1)]
        [snail_list.append(snail_map[i][lowerLimit])   for i in range(upperLimit-2,lowerLimit,-1)]
        lowerLimit += 1
        upperLimit -= 1
        
    return snail_list
           


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
array = [[]]
#expected = [1,2,3,6,9,8,7,4,5]
print(snail(array))