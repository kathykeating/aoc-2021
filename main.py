# coding=utf-8
# This is a sample Python script.
import csv


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def calc_change(prior, current):
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


# Get the Sea Depth readings
def read_sea_depth():
    f = open("sea_depth.csv", "r")
    csv_reader = csv.reader(f)

    list_depth = []
    for row in csv_reader:
        list_depth.append(row[0])
    print(list_depth)
    return list_depth


def determine_increase(list_depth):
    prior = 0
    count_increase = 0
    for item in list_depth:
        change = calc_change(prior, item)
        if change == "increase":
            count_increase += 1
        prior = int(item)
    return count_increase


def build_ranges(list_depth):
    length = len(list_depth)
    print length

    list_range = []
    for idx, row in enumerate(list_depth):
        if idx + 2 < length:
            the_range = int(list_depth[idx]) + int(list_depth[idx+1]) + int(list_depth[idx+2])
            list_range.append(the_range)
    print(list_range)
    print len(list_range)
    return list_range


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    depth = read_sea_depth()
    increase = determine_increase(depth)
    print("Sea Depth Change=%d", increase) # 1564

    # three count ranges
    ranges = build_ranges(depth)
    increase = determine_increase(ranges)
    print("Sea Depth Range Change=%d", increase)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
