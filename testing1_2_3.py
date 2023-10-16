def number(lines):
    result = []
    counter = 1
    # loop through array item by item
    for x in lines:
        # take each item and add a number and colon in front ("n: x"), start counting from 1
        y = str(counter) + ": " + x
        # append new item to "result" array
        result += [y]
        counter += 1

    return result


number(["a", "b", "c"])
