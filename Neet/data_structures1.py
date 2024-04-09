# Design Dynamic Array (Resizable Array)
# Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

# Your DynamicArray class should support the following operations:

# DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
# int get(int i) will return the element at index i. Assume that index i is valid.
# void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
# void pushback(int n) will push the element n to the end of the array.
# int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
# void resize() will double the capacity of the array.
# int getSize() will return the number of elements in the array.
# int getCapacity() will return the capacity of the array.
# If we call void pushback(int n) but the array is full, we should resize the array first.

# Example 1:

# Input:
# ["Array", 1, "getSize", "getCapacity"]

# Output:
# [null, 0, 1]
# Example 2:

# Input:
# ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

# Output:
# [null, null, 1, null, 2]
# Example 3:

# Input:
# ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]

# Output:
# [null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]
# Note:

# The index i provided to get(int i) and set(int i) is guranteed to be greater than or equal to 0 and less than the number of elements in the array.

class DynamicArray:

    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Pop from empty array")
        val = self.array[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


# commands = ["Array", 1, "getSize", "getCapacity"]
# commands = ["Array", 1, "pushback", 1,
#             "getCapacity", "pushback", 2, "getCapacity"]
commands = ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback",
            2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]

my_array = DynamicArray(commands[1])
results = [None]

method_arg_counts = {
    "pushback": 1,
}


i = 2
while i < len(commands):
    cmd = commands[i]
    i += 1

    method = getattr(my_array, cmd, None)
    if method is None:
        continue

    args = []
    while i < len(commands) and (isinstance(commands[i], int) or isinstance(commands[i], tuple)):
        args.append(commands[i])
        i += 1

    if args:
        result = method(*args)
    else:
        result = method()

    results.append(result)

print(results)
