class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            closest_lesser_no = [x for x in nums if x < target]
            if not closest_lesser_no:
                return 0
            return nums.index(max(closest_lesser_no))+1


solution = Solution()
print("Test 1: ", solution.searchInsert([1, 3, 5, 6], 5))  # out: 2
print("Test 2: ", solution.searchInsert([1, 3, 5, 6], 2))  # out: 1
print("Test 3: ", solution.searchInsert([1, 3, 5, 6], 999))  # out: 4
print("Test 4: ", solution.searchInsert([1, 3, 5, 6], 0))  # out: 0
print("Test 5: ", solution.searchInsert([-1, 3, 5, 6], 0))  # out: 1
