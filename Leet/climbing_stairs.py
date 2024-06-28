class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


solution = Solution()
print("Test 1: ", solution.climbStairs(2))  # should output: 2
print("Test 2: ", solution.climbStairs(3))  # should output: 3
print("Test 3: ", solution.climbStairs(5))  # should output: 8
