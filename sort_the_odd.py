# Task
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    if source_array == []:
        return []

    # extract odd array
    odd_array = []
    for num in source_array:
        if num % 2 != 0:
            odd_array.append(num)

    # sort odd array
    sorted_odd_array = sorted(odd_array)

    # replace every odd number in original array
    counter = 0
    for index1, odd in enumerate(source_array):
        if odd % 2 != 0:
            source_array[index1] = sorted_odd_array[counter]
            counter += 1

    return source_array


print(sort_array([5, 3, 2, 8, 1, 4]))  # should output: [1, 3, 2, 8, 5, 4]
print(sort_array([5, 3, 1, 8, 0]))  # should output: [1, 3, 5, 8, 0]
print(sort_array([]))  # should output: []
