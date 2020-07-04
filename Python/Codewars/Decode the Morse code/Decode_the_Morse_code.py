def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    tokenCode = morse_code.replace('   ', ' & ')
    characterList = tokenCode.split(' ')
    words = ''
    for counter in range(0,len(characterList)):
        if characterList[counter] == '&':
            words = words + ' '
        else:
            words = words + MORSE_CODE[characterList[counter]]
    
    return words

decodeMorse('.... . -.--   .--- ..- -.. .')