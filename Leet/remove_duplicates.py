class Solution:
    def removeDuplicates(self, nums) -> int:
        expectedNums = []
        for num in nums:
            if num not in expectedNums:
                expectedNums.append(num)
            else:
                expectedNums.append(30001)

        nums[:] = sorted(expectedNums)
        k = len([element for element in nums if element != 30001])

        return k


solution = Solution()
print("Test 1: ", solution.removeDuplicates([1, 1, 2]))
# test_1 should return [1,2,"_"]
