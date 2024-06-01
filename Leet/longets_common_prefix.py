class Solution:
    def longestCommonPrefix(self, strs):
        if strs == [""]:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            # find shortes word and trim all words to same length
            min_length = min(len(word) for word in strs)
            trimmed_words = [word[:min_length] for word in strs]

            # take first word
            longest_common_prefix = trimmed_words[0]

            # compare each letter from first word with the next word
            for word in trimmed_words[1:]:
                if longest_common_prefix == '' or word == '':
                    break
                if longest_common_prefix[0] != word[0]:
                    longest_common_prefix = ''
                    break
                else:
                    for number in range(len(longest_common_prefix)):
                        if longest_common_prefix[number] == word[number]:
                            continue
                        else:
                            longest_common_prefix = longest_common_prefix[:number]
                            break

            return longest_common_prefix


solution = Solution()
test_1 = ["flower", "flow", "flight"]
test_2 = ["dog", "racecar", "car"]
test_3 = ["amongst", "an", "array"]
test_4 = ["acc", "aaa", "aaba"]
print("Test 1: ", solution.longestCommonPrefix(test_1))
print("Test 2: ", solution.longestCommonPrefix(test_2))
print("Test 3: ", solution.longestCommonPrefix(test_3))
print("Test 4: ", solution.longestCommonPrefix(test_4))
