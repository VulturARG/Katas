# https://www.codewars.com/kata/5886e082a836a691340000c3/train/python

import math


def rectangle_rotation(a, b):
    cos_45 = 0.7071067811865475
    x1 =  cos_45 / 2 *(a - b)
    y1 =  cos_45 / 2 *(a + b)
    
    x2 =  cos_45 / 2 *(b + a)
    y2 =  cos_45 / 2 *(a - b)
    
    x3 =  cos_45 / 2 *(-a + b)
    y3 =  cos_45 / 2 *(-a - b)
    
    x4 =  cos_45 / 2 *(-b - a)
    y4 =  cos_45 / 2 *(-a + b)
    
    max_x = math.ceil(max(x1,x2,x3,x4))
    min_x = math.floor(min(x1,x2,x3,x4))
    max_y = math.ceil(max(y1,y2,y3,y4))
    min_y = math.floor(min(y1,y2,y3,y4))
    
    Crsu = y1 - x1
    Crde = y1 + x1
    Crin = y3 - x3
    Criz = y3 + x3
    
    points = 0
    
    for x in range(min_x,max_x):
        for y in range(min_y,max_y):
            yrsu =  x + Crsu
            yrde = -x + Crde
            yrin =  x + Crin
            yriz = -x + Criz
            
            if y < yrsu and y < yrde and y > yrin and y > yriz:
                points += 1
    
    return points
    
    
    

print(rectangle_rotation(6,4))

'''
Test.it("Basic Tests")
Test.assert_equals( rectangle_rotation(6,4),23)
Test.assert_equals( rectangle_rotation(30,2),65)
Test.assert_equals( rectangle_rotation(8,6),49)
Test.assert_equals( rectangle_rotation(16,20),333)
'''