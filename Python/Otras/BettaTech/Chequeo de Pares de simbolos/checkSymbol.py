def check_symbol_open_close(string):
    open_symbol = ['(','{','[']
    close_symbol = [')','}',']']
    
    while (len(string) > 0):
        print(string)
        previus_symbol = string[0]
        position = open_symbol.index(previus_symbol)
        search_symbol = close_symbol[position]
        position = find_right_symbol(string, previus_symbol, search_symbol)
        if position != -1:
            new_string = string[1:position]
            if position != len(string):
                string = string[position+1:]
            else:
                string = '';
            if len(new_string) == 0 and len(string) == 0: return True
            if len(new_string) %  2 !=0: return False
            check = check_symbol_open_close(new_string)
            if not check: return False
        else:
            return False
    
    return True

def find_right_symbol(string, previus_symbol, search_symbol):
    count = 0
    for i in range(len(string)):
        if string[i] == previus_symbol: count += 1
        if string[i] == search_symbol: count -= 1
        if count == -1: return -1
        if count == 0: return i

    return -1


