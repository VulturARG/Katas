def valid_parentheses(string):
    count = 0
    for i in range(len(string)):
        if string[i] != '(': count += 1
        if string[i] != ')': count -= 1
        if count == -1: return False

    return True if count == 0 else False