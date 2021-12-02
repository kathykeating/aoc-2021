# coding=utf-8
# Advent of Code 2021 - Day 1
import utils

class Location:
  def __init__(self, forward, depth, aim):
    self.forward = forward
    self.depth = depth
    self.aim = aim


# Determine the Location
def determine_location(movement):
    position = Location(0,0,0)
    for direction, units in movement:
        if direction == "up":
            position.depth -= int(units)
        elif direction == "down":
            position.depth += int(units)
        else:
            position.forward += int(units)

    return position

# Determine the Location with aim
def determine_aim(movement):
    position = Location(0,0,0)
    for direction, units in movement:
        if direction == "up":
            position.aim -= int(units)
        elif direction == "down":
            position.aim += int(units)
        else:
            position.forward += int(units)
            position.depth += int(units) * position.aim

    return position

def main_day2():
    # DAY 2 ----------------------------------------------------------
    print('\n\n***** DAY 2 *****')
    # process location after movement
    moves = utils.read_file("movement.csv", "row", ' ')
    # print(moves)

    # calculate location
    location = determine_location(moves)
    print('Location:\n  Forward = {0}\n  Depth = {1}\n  Combined = {2}'
          .format(location.forward, location.depth, location.forward * location.depth)) # 1524750

    # calculate aim
    aim = determine_aim(moves)
    print('\nLocation with Aim:\n  Forward = {0}\n  Depth = {1}\n  Combined = {2}'
          .format(aim.forward, aim.depth, aim.forward * aim.depth))  # 1592426537

