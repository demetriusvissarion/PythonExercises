# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    if text:
        cleaned_string = ""
        for char in text:
            if char.isalpha():
                cleaned_string += char
            else:
                cleaned_string += " "

        cleaned_list = cleaned_string.split(' ')

        result = [cleaned_list[0]]
        for i in range(1, len(cleaned_list)):
            result.append(cleaned_list[i].title())

        return ''.join(result)
    else:
        return ''


print(to_camel_case(''))
print(to_camel_case('the_stealth_warrior'))
print(to_camel_case('The-Stealth-Warrior'))
print(to_camel_case('A-B-C'))
