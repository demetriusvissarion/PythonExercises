class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        sample = list(words[0])

        for word in words[1:]:
            new_sample = []
            for char in word:
                if char in sample:
                    new_sample.append(char)
                    sample.remove(char)
            sample = new_sample

        return sample


test_1 = ["bella", "label", "roller"]
solution = Solution()
print(solution.commonChars(test_1))
