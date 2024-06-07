class Solution:
    def plusOne(self, digits):
        # # list of strings
        # list_of_strings = [str(i) for i in digits]
        # # concatenate strings into one string
        # concatenated_string = "".join(list_of_strings)
        # # turn string into digit and add 1
        # return [int(i) for i in str(int(concatenated_string) + 1)]

        return [int(i) for i in str(int("".join([str(i) for i in digits])) + 1)]


solution = Solution()
print("Test 1: ", solution.plusOne([1, 2, 3]))  # out: [1, 2, 4]
print("Test 2: ", solution.plusOne([4, 3, 2, 1]))  # out: [4, 3, 2, 2]
print("Test 3: ", solution.plusOne([9]))  # out: [1, 0]
