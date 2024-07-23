from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = [x for x in nums1[:m]] + nums2
        nums1.sort()


solution = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution.merge(nums1, m, nums2, n)

print("Test 1: ", nums1)
# test_1 should return [1,2,2,3,5,6]
