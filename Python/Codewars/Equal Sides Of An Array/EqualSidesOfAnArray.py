def find_even_index(arr):
    lenArr = len(arr)
    for n in range(lenArr):
        leftSum = sum(arr[0:n]) if n > 0 else 0
        rightSum = sum(arr[n+1:lenArr]) if n < lenArr else 0
        if leftSum == rightSum:
            return n
    return -1

print(find_even_index([10,-80,10,10,15,35,20]))