# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

# Example
# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
# Note
# In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.

def count_smileys(arr):
    result = 0

    for face in arr:
        if len(face) == 2:
            if face[0] in [':', ';'] and face[1] in [')', 'D']:
                result += 1
        elif len(face) == 3:
            if face[0] in [':', ';'] and face[1] in ['-', '~'] and face[2] in [')', 'D']:
                result += 1

    return result


print(count_smileys([]))  # 0
print(count_smileys([':D', ':~)', ';~D', ':)']))  # 4
print(count_smileys([':)', ':(', ':D', ':O', ':;']))  # 2
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))  # 1
