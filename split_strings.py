# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    result = [s[i:i+2] for i in range(0, len(s), 2)]
    if result == []:
        result == []
    elif len(result) == 1 and len(list(result[0])) == 1:
        result[0] = result[0] + "_"
    elif len(list(result[-1])) == 1:
        result[-1] = result[-1] + "_"
    return result


print(solution("asdfadsf"))  # should outoput: ['as', 'df', 'ad', 'sf']
print(solution("asdfads"))  # should outoput: ['as', 'df', 'ad', 's_']
print(solution(""))  # should outoput: []
print(solution("x"))  # should outoput: ["x_"]
