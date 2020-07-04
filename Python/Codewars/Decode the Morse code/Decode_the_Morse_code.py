def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    #return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
    tokenCode = morse_code.replace('   ', '&')
    characterList = tokenCode.split(' ')
    print(characterList)
    #characterList = characterList.replace('&',' ')
    words = ''
    for counter in range(0,len(characterList)):
        character = characterList[counter]
        words = words + MORSE_CODE[characterList[counter]]
    
    return words