class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        min1 = 0
        max1 = x

        while min1 <= max1:
            mid = (min1 + max1) // 2
            res = mid ** 2
            if res == x:
                return mid
            elif res > x:
                max1 = mid - 1
            else:
                min1 = mid + 1

        return max1


solution = Solution()
print("Test 1: ", solution.mySqrt(4))  # should output: 2
print("Test 2: ", solution.mySqrt(8))  # should output: 2
print("Test 3: ", solution.mySqrt(0))  # should output: 0
print("Test 4: ", solution.mySqrt(1))  # should output: 1
print("Test 5: ", solution.mySqrt(2**31 - 1))  # should output: 46340
