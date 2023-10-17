def persistence(num):
    array = list(str(num))
    counter = 0
    result = 1
    if len(array) <= 1:
        return 0
    else:
        while len(array) > 1:
            for x in array:
                result = result * int(x)
            array = list(str(result))
            result = 1
            counter += 1
    return counter


print(persistence(39))
print(persistence(25))
print(persistence(4))
print(persistence(999))
