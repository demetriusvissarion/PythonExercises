def array_diff(a, b):
    return [x for x in a if x not in b]


print(array_diff([1, 2], [1]))
print(array_diff([1, 2], [2]))
print(array_diff([1, 2, 2], [1]))
print(array_diff([1, 2, 2], [2]))
