'''
Dado una lista de años de nacimiento y muerte de personas buscar el año mas poblado
'''


def search_year(arr):
    poblation = {}
    for person in arr:
        if person[0] in poblation:
            poblation[person[0]] += 1
        else:
            poblation[person[0]] = 1
        
        if person[1] in poblation:
            poblation[person[1]] -= 1
        else:
            poblation[person[1]] = -1
    
    poblation_sort = sorted(poblation.items())
    
    max_poblation_year = 0
    max_poblation = 0
    sum = 0
    for year, value in poblation_sort:
        sum += value
        if max_poblation < sum:
            max_poblation = sum
            max_poblation_year = year
                
    return [max_poblation_year,max_poblation]