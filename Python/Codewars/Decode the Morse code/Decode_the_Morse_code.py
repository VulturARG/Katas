def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    #return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
    while morse_code.startswith(' '):
        morse_code = morse_code[1:len(morse_code)]
    tokenCode = morse_code.replace('   ', ' & ')
    characterList = tokenCode.split(' ')
    words = ''
    for counter in range(len(characterList)):
        if characterList[counter] == '':
            continue
        elif characterList[counter] == '&':
            words += ' '
        else:
            words += 'E'#words += MORSE_CODE[characterList[counter].replace(' ', '')]
    return words

#print(decodeMorse(' . '))
print(decodeMorse('   .   . '))