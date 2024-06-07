class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Solution 1:
        # return str(bin(int(a, 2) + int(b, 2))[2:])

        # Solution 2: without using built in function ####
        # reverse a and b strings
        rev_a = a[::-1]
        rev_b = b[::-1]

        # adjust to max length by adding zero prefixes (zero addition doesn't change the outcome)
        max_len = max(len(rev_a), len(rev_b))
        rev_a = rev_a.ljust(max_len, '0')
        rev_b = rev_b.ljust(max_len, '0')

        # declare result and carry variables
        result = ''
        carry = 0

        # loop range(max(len(a),len(b))) and write addition rules
        for i in range(max_len):
            if rev_a[i] == '0' and rev_b[i] == '0':
                if carry == 1:
                    result = '1' + result
                    carry = 0
                else:
                    result = '0' + result
            elif (rev_a[i] == '0' and rev_b[i] == '1') or (rev_a[i] == '1' and rev_b[i] == '0'):
                if carry == 1:
                    result = '0' + result
                    carry = 1
                else:
                    result = '1' + result
            elif rev_a[i] == '1' and rev_b[i] == '1':
                if carry == 1:
                    result = '1' + result
                else:
                    result = '0' + result
                    carry = 1

        if carry:
            result = '1' + result

        return result


solution = Solution()
print("Test 1: ", solution.addBinary("11", "1"))  # should output: "100"
print("Test 2: ", solution.addBinary("1010", "1011"))  # should output: "10101"
