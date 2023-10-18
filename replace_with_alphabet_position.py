# Given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

def alphabet_position(text):
    result = []
    text = [*(''.join(x for x in text if x.isalpha()).lower())]
    for index, letter in enumerate(text):
        result.append(ord(letter) - 96)
    return str(result).translate(str.maketrans('', '', '[],\''))


print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))
