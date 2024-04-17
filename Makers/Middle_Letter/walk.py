def ten_minute_walk(directions):
    if len(directions) != 10:
        return False

    north_south = 0
    east_west = 0

    for direction in directions:
        if direction == 'n':
            north_south += 1
        elif direction == 's':
            north_south -= 1
        elif direction == 'e':
            east_west += 1
        elif direction == 'w':
            east_west -= 1

    return north_south == 0 and east_west == 0


print(ten_minute_walk(['w', 's', 'e', 'e', 'n',
      'n', 'e', 's', 'w', 'w']))  # => true
print(ten_minute_walk(['w', 's', 'e', 'n', 'n',
      'e', 's', 'w', 'w', 'w']))  # => false
print(ten_minute_walk(['w', 's', 'e', 's', 's',
      'e', 's', 'w', 'n', 'n']))  # => false
print(ten_minute_walk(['w', 's']))  # => false
