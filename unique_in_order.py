# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
    sequence = [*sequence]
    result = []
    if len(sequence) == 1:
        return sequence
    for index, item in enumerate(sequence):
        if index == 0:
            result.append(item)
        elif item != sequence[index-1]:
            result.append(item)
    return result


# Should work with empty sequence
print(unique_in_order(""))  # should output []
print(unique_in_order([]))  # should output []
print(unique_in_order(()))  # should output []

# Should work with single element sequence
print(unique_in_order("A"))  # should output ["A"]
print(unique_in_order(["A"]))  # should output ["A"]
print(unique_in_order(("A",)))  # should output ["A"]

# Should reduce duplicates
print(unique_in_order("AA"))  # should output ["A"]
print(unique_in_order("AAAABBBCCDAABBB"))  # ["A", "B", "C", "D", "A", "B"]
