def get_middle(word):
    middle_letter = ""
    # if even
    if len(word) % 2 == 0:
        # print("len(word): ", len(word))
        middle_letter += word[len(word) // 2 - 1]
        middle_letter += word[len(word) // 2]
    # if odd
    else:
        middle_letter += word[round(len(word) // 2)]

    return middle_letter


print("get_middle('test'): ", get_middle("test"))  # => "es"
print("get_middle('testing'): ", get_middle("testing"))  # => "t"
print("get_middle('middle'): ", get_middle("middle"))  # => "dd"
print("get_middle('A'): ", get_middle("A"))  # => "A"
print("get_middle('of'): ", get_middle("of"))  # => "of"
