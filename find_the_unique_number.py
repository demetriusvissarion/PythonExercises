# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    numbers = list(set(arr))
    new_array = []
    counter = 0
    while counter < 3:
        new_array.append(arr[counter])
        counter += 1
    if new_array.count(numbers[0]) > 1:
        return numbers[1]
    else:
        return numbers[0]


print(find_uniq([1, 1, 1, 2, 1, 1]))  # 2
print(find_uniq([0, 0, 0.55, 0, 0]))  # 0.55
print(find_uniq([3, 10, 3, 3, 3]))  # 10
