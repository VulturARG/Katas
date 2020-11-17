# Dado un array que representa un número sumar uno a ese número
# https://www.youtube.com/watch?v=uQdy914JRKQ

def plus_one(arr):
    if len(arr) == 0: return [1]
    new_array = []
    digit = arr.pop()
    if digit == 9:
        new_array = plus_one(arr) + [0]
    else:
        new_array = arr + [digit+1]
    
    return new_array
