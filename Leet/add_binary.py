class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))[2:])


solution = Solution()
print("Test 1: ", solution.addBinary("11", "1"))  # should output: "100"
print("Test 2: ", solution.addBinary("1010", "1011"))  # should output: "10101"
