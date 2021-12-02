# coding=utf-8
# This is a sample Python script.
import csv

class Location:
  def __init__(self, forward, depth, aim):
    self.forward = forward
    self.depth = depth
    self.aim = aim

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def read_file(file_name, type, delimit):
    f = open(file_name, "r")
    csv_reader = csv.reader(f, delimiter=delimit)

    list_depth = []
    for row in csv_reader:
        if type == "row":
            list_depth.append(row)
        else:
            list_depth.append(row[0])
    return list_depth


# calculates depth change direct
def calc_direction(prior, current):
    # set prior to current if we're at the beginning of the list
    if prior == 0:
        prior = int(current)

    # determine the difference
    diff = int(current) - prior
    if diff < 0:
        change = 'decrease'
    elif diff == 0:
        change = 'same'
    else:
        change = 'increase'
    return change


# Determine the increase across the entire depth
def determine_increase(list_depth):
    prior = 0
    count_increase = 0
    for item in list_depth:
        change = calc_direction(prior, item)
        if change == "increase":
            count_increase += 1
        prior = int(item)
    return count_increase


# Determine the increase by rolling 3-step ranges
def build_ranges(list_depth):
    length = len(list_depth)

    list_range = []
    for idx, row in enumerate(list_depth):
        if idx + 2 < length:
            the_range = int(list_depth[idx]) + int(list_depth[idx+1]) + int(list_depth[idx+2])
            list_range.append(the_range)
    return list_range


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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # calculate the full increase across the depth
    depth = read_file("sea_depth.csv", "field", ',')
    #  print(depth)
    increase = determine_increase(depth)
    print('Sea Depth Change = {0}'.format(increase))  # 1564

    # calculate three count ranges
    ranges = build_ranges(depth)
    #  print(ranges)
    increase = determine_increase(ranges)
    print('Sea Depth Range Change = {0}'.format(increase))  # 1611

    # process location after movement
    moves = read_file("movement.csv", "row", ' ')
    print(moves)

    location = determine_location(moves)
    print('Location:\n  Forward = {0}\n  Depth = {1}\n  Combined = {2}'
          .format(location.forward, location.depth, location.forward * location.depth)) # 1524750

    aim = determine_aim(moves)
    print('Location:\n  Forward = {0}\n  Depth = {1}\n  Combined = {2}'
          .format(aim.forward, aim.depth, aim.forward * aim.depth))  # 1592426537

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
