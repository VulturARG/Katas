def meeting(s):
    listString = s.upper().split(';')
    for i,name in enumerate(listString):
        listString[i] = name.split(':')
        listString[i].reverse()
    sortedList = sorted(sorted(listString,key=lambda x: x[1]),key=lambda x: x[0])
    sortedString = ''
    for name in sortedList:
        sortedString += f'({name[0]}, {name[1]})'
    return sortedString
    


s = "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
print(meeting(s))
    