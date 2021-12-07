# coding=utf-8
# Advent of Code 2021 - Day 6
import utils, sys, csv
import submarine

def main_day6():
    sub = submarine.Submarine()

    lanternfish = utils.read_file("./data/lanternfish.csv", "row", ',')[0]
    lanternfish = [int(x) for x in lanternfish]
    print lanternfish

    # build an array by age of the fish
    fishes = [0 for x in range(9)]
    for f in lanternfish:
        fishes[int(f)] += 1
    print(fishes)

    # iterate through the days
    for i in range(80):
        fishes = count_fishes(fishes)

    numfish = 0
    for x in range(9):
        numfish += fishes[x]
    print('Lanternfish after 80 days\n')
    print (' Number of Fish= {0}'.format(numfish))

    for i in range(256-80):
        fishes = count_fishes(fishes)

    numfish = 0
    for x in range(9):
        numfish += fishes[x]
    print('Lanternfish after 256 days\n')
    print (' Number of Fish= {0}'.format(numfish))


def count_fishes(fishes):
    temp = [0 for x in range(9)]
    for day in range(9):
        if day == 0:  # spawn
            temp[8] += fishes[day]  # create new fish
        else:
            temp[day - 1] = fishes[day]  # age the fishes maturity cycle
    temp[6] += temp[8]  # reset the parents' mating cycle

    # transfer
    for x in range(9):
        fishes[x] = temp[x]

    return fishes