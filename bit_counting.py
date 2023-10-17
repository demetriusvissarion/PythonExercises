# def count_bits(n):
#     result = 0
#     for x in bin(n)[2:]:
#         result += int(x)
#     return result

def count_bits(n):
    return sum(int(x) for x in bin(n)[2:])


print(count_bits(0))
print(count_bits(4))
print(count_bits(7))
print(count_bits(9))
print(count_bits(10))
