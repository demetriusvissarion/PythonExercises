class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_a = int(a, 2)
        dec_b = int(b, 2)
        dec_sum = dec_a + dec_b
        return str(bin(dec_sum)[2:])


solution = Solution()
print("Test 1: ", solution.addBinary("11", "1"))  # should output: "100"
print("Test 2: ", solution.addBinary("1010", "1011"))  # should output: "10101"
