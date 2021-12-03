# coding=utf-8
# Advent of Code 2021 - Day 1
import utils

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


def main_day1():
    # DAY 1 ----------------------------------------------------------
    print('***** DAY 1 *****')
    # calculate the full increase across the depth
    depth = utils.read_file("./data/sea_depth.csv", "field", ',')
    #  print(depth)
    increase = determine_increase(depth)
    print('Sea Depth Change = {0}'.format(increase))  # 1564

    # calculate three count ranges
    ranges = build_ranges(depth)
    #  print(ranges)
    increase = determine_increase(ranges)
    print('Sea Depth Range Change = {0}'.format(increase))  # 1611