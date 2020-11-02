# http://codingdojo.org/kata/StringCalculator/

def add(numbers):
    try:
        return "Number expected but '\n' found at position "+str(numbers.index(',\n')+1)+"."
    except ValueError: 
        if numbers == "":
            return "0"
        else:
            result = 0
            delimiter = ','
            negative_numbers =[]
            numbers_lines = numbers.splitlines()
            if numbers_lines[0].startswith('//'):
                delimiter = numbers_lines.pop(0)
                delimiter = delimiter.replace('//','')
            for line in numbers_lines:
                if line[-1] != delimiter:
                    numbers_list = line.split(delimiter)
                    for number in numbers_list:
                        try:
                            float_number = float(number)
                            if float_number < 0:
                                negative_numbers.append(number)
                            result += float_number
                        except:
                            #print(number)
                            invalid_char = None
                            for character in number:
                                if not character.isdigit():
                                    invalid_char = character
                            index = line.index(invalid_char)
                            return f"'{delimiter}' expected but '{invalid_char}' found at position {index}."
                else:
                    return "Number expected but EOF found."

            if negative_numbers:
                return f"Negative not allowed : {', '.join(negative_numbers)}"
            else:    
                return str(round(result)) if round(result) == result else f'{result:.1f}'
        
        return None

#add("//;\n1;2")
print("----------------------------------")
add("//|\n1|2,3")
#print("----------------------------------")
#add("1,3,")