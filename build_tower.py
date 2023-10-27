# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]

# And a tower with 6 floors looks like this:
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]

def tower_builder(n_floors):
    tower = []
    for floor in range(1, 2 * n_floors, 2):
        tower.append((floor * '*').center((n_floors * 2) - 1))

    return tower


print(tower_builder(1))  # ['*', ]
print(tower_builder(2))  # [' * ', '***']
print(tower_builder(3))  # ['  *  ', ' *** ', '*****']
