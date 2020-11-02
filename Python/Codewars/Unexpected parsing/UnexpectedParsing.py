def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return status

def comfortable_word(word):
    left = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c']
    right = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
    side = None
    for leter in word:
        try:
            left.index(leter)
            newSide = 'left'
        except:
            #right.index(leter)
            newSide = 'right'
        if side == None:
            side = newSide
        elif side == newSide:
            return False
        else:
            side = newSide
    return True

#print(get_status(True))
#print(get_status(False))
word = 'embl'
print(comfortable_word(word))
print('+'*3)