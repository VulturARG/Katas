#https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

def cakes(recipe, available):
    minumun = 10000000000000
    index_value = 0
    for n in recipe:
        try:
            divisor = int(available[n]/recipe[n])
        except:
            return 0
        minumun = minumun if minumun < divisor else divisor
        
    return minumun

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

#print(cakes(recipe, available))
