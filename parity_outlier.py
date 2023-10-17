def find_outlier(integers):
    odds_array = []
    evens_array = []
    for num in integers:
        evens_array.append(num) if ((num % 2) == 0) else odds_array.append(num)
    return int((odds_array if (len(odds_array) < len(evens_array)) else evens_array)[0])


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
