# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.


def high(x):
    # split string into array of words
    words_array = x.split()

    # create scores array with equal no. of elements all starting at 0
    word_scores = [0] * len(words_array)

    # loop through words_array, calculate and save each word score
    for index, word in enumerate(words_array):
        for letter in word:
            word_scores[index] += ord(letter)-96

    # find word with highest score
    return str(words_array[word_scores.index(max(word_scores))])


print(high('man i need a taxi up to ubud'))  # 'taxi'
print(high('what time are we climbing up the volcano'))  # 'volcano'
print(high('take me to semynak'))  # 'semynak'
print(high('aa b'))  # 'aa'
print(high('b aa'))  # 'b'
print(high('bb d'))  # 'bb'
print(high('d bb'))  # 'd'
print(high("aaa b"))  # "aaa"
