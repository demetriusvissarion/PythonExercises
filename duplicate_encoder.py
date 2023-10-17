def duplicate_encode(word):
    list = [*word.lower()]
    return ''.join([')' if y in set([x for x in list if list.count(x) > 1]) else '(' for x, y in enumerate(list)])


print(duplicate_encode('din'))
