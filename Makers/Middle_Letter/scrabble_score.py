class Scrabble:
    def __init__(self, word=""):
        if word is None:
            word = ""
        self.word = self.clean_word(word)
        self.score = 0
        self.calculate_score()

    @classmethod
    def new(cls, word):
        return cls(word)

    def clean_word(self, word):
        return ''.join(filter(str.isalpha, word)).upper()

    def calculate_score(self):
        case_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
        case_2 = ["D", "G"]
        case_3 = ["B", "C", "M", "P"]
        case_4 = ["F", "H", "V", "W", "Y"]
        case_5 = ["K"]
        case_8 = ["J", "X"]
        case_10 = ["Q", "Z"]

        for letter in self.word:
            if letter in case_1:
                self.score += 1
            elif letter in case_2:
                self.score += 2
            elif letter in case_3:
                self.score += 3
            elif letter in case_4:
                self.score += 4
            elif letter in case_5:
                self.score += 5
            elif letter in case_8:
                self.score += 8
            elif letter in case_10:
                self.score += 10


scrabble = Scrabble.new('')
print("score for '': ", scrabble.score)  # => 0

scrabble = Scrabble.new(" \t\n")
print("score for ' \t\n': ", scrabble.score)  # => 0

scrabble = Scrabble.new(None)
print("score for 'None': ", scrabble.score)  # => 0

scrabble = Scrabble.new('a')
print("score for 'a': ", scrabble.score)  # => 1

scrabble = Scrabble.new('f')
print("score for 'f': ", scrabble.score)  # => 4

scrabble = Scrabble.new('street')
print("score for 'street': ", scrabble.score)  # => 6

scrabble = Scrabble.new('quirky')
print("score for 'quirky': ", scrabble.score)  # => 22

scrabble = Scrabble.new('OXYPHENBUTAZONE')
print("score for 'OXYPHENBUTAZONE': ", scrabble.score)  # => 41
