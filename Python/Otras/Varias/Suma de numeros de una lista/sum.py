'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
# O(n^2)???
def sum_search(arr,number):
    if len(arr) == 0: return False
    for i in arr:
        diff = number - i
        if diff in arr:
            return True
    
    return False

#Google solution https://www.youtube.com/watch?v=XKu_SEDAykw
# La lista esta ordenada
#O(n)
def sum_search_google(arr,number):
    first_index = 0
    last_index = len(arr) - 1
    while first_index <  last_index:
        compare_number = arr[first_index] + arr[last_index] - number
        if compare_number == 0:
            return True
        elif compare_number < 0:
            first_index += 1
        else:
            last_index -=1
    
    return False

#ordeno la lista previamente
#O(n log n)
def order_first(arr,number):
    return sum_search_google(sorted(arr),number)

#Lista no ordenada video google
def sum_search_google_no_order(arr,number):
    complement = set()
    for value in arr:
        if value in complement:
            return True
        
        complement.add(number-value)
    
    return False