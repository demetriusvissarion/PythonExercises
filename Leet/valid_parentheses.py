class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False

        return stack == []


solution = Solution()
test_1 = "()"  # should return true
test_2 = "()[]{}"  # should return true
test_3 = "(]"  # should return false
test_4 = "([)]"  # should return false
print("Test 1: ", solution.isValid(test_1))
print("Test 2: ", solution.isValid(test_2))
print("Test 3: ", solution.isValid(test_3))
print("Test 4: ", solution.isValid(test_4))
