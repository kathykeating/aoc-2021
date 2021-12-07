# coding=utf-8
# Advent of Code 2021 - Day 7
import utils, sys, csv
import submarine

def main_day7():
    sub = submarine.Submarine()

    crabs = utils.read_file("./data/crabs.csv", "row", ',')[0]
    crabs = [int(x) for x in crabs]
    print crabs

    median = get_median(crabs)

    print 'Align the Crabs\n'
    print ('  Crab Count = {0}\n  Median = {1}'.format(len(crabs), median))

    fuel = 0
    for crab in crabs:
        fuel += abs(crab - median)

    print('  Fuel Used = {0}'.format(fuel)) # 344297

    # incremental fuel usage
    each = []
    for position in range(len(crabs)):
        distance = [abs(crab - position) for crab in crabs]
        diffs = sum([sum(list(range(dif + 1))) for dif in distance])
        each.append(diffs)

    print('  Optimal Position = {0}'.format(get_optimal(crabs)))  #

def get_median(list):
    n = len(list)
    list.sort()

    if n % 2 == 0:
        median1 = list[n // 2]
        median2 = list[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = list[n // 2]
    return median

def get_optimal(data):
    l = len(data)
    f = []

    for v in range(l):
        diff = [abs(d - v) for d in data]
        diffs = sum([sum(list(range(dif + 1))) for dif in diff])
        f.append(diffs)
    return min(f)