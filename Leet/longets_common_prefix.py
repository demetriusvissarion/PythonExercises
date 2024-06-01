class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        shortest_word = min(strs, key=len)

        for i, char in enumerate(shortest_word):
            for word in strs:
                if word[i] != char:
                    return shortest_word[:i]

        return shortest_word


solution = Solution()
test_1 = ["flower", "flow", "flight"]
test_2 = ["dog", "racecar", "car"]
test_3 = ["amongst", "an", "array"]
test_4 = ["acc", "aaa", "aaba"]
print("Test 1: ", solution.longestCommonPrefix(test_1))
print("Test 2: ", solution.longestCommonPrefix(test_2))
print("Test 3: ", solution.longestCommonPrefix(test_3))
print("Test 4: ", solution.longestCommonPrefix(test_4))
