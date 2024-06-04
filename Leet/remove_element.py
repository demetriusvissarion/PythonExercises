class Solution:
    def removeElement(self, nums, val: int) -> int:
        nums[:] = [num for num in nums if num != val]
        return len(nums)


# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
solution = Solution()
print("Test 1: ", solution.removeElement([3, 2, 2, 3], 3))
