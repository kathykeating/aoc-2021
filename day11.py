# coding=utf-8
# Advent of Code 2021 - Day 11
import utils, sys, csv
import submarine

def main_day11():
    sub = submarine.Submarine()
    octopus = get_data("./data/dumbo_octopus.txt")
    flash_count = 0
    current_count = 0

    view_octopus(0, octopus)
    for n in range(1, 1000): # 100
        current_count = observe(n, octopus)
        flash_count += current_count

        if n == 100:
            view_octopus(n, octopus)
            print "Flashes after 100 Rotations"
            print " Count of Flashes = {0}".format(flash_count) # 1679

        # continue until we get all octopi flashing
        if len(octopus[0]) * len(octopus) == current_count:
            break

    view_octopus(n, octopus)
    print "Synchronicity"
    print " Count of Flashes = {0}".format(n) # 519


def get_data(filename):
    with open(filename) as file:
        string_list = file.read().splitlines()

    data = [[0] for x in range(len(string_list))]
    for n, line in enumerate(string_list):
        data[n] = list(map(int, [char for char in line]))
        # data[n] = [char for char in line]
    return data


def view_octopus(round, octopi):
    print "\n** {0} **".format(round)
    for row in octopi:
        print ''.join([str(x) for x in row])


def reset_octopus(octopi):
    for row, line in enumerate(octopi):
        for col, char in enumerate(line):
            if octopi[row][col] == 'X':
                octopi[row][col] = 0


def observe(rotation, octopus):
    for row, line in enumerate(octopus):
        for col, char in enumerate(line):
            if octopus[row][col] == 9:
                octopus[row][col] = 'X'
                cascade(octopus, row, col)
            elif octopus[row][col] < 9:
                octopus[row][col] += 1

    current_count = count_flashes(octopus)
    reset_octopus(octopus)  # whew! they are tired from flashing, start them over again
    # view_octopus(rotation, octopus)
    return current_count





def increase_power(row, col, octopi):
    if octopi[row][col] < 9:  # give it a boost but it doesn't cascade
        octopi[row][col] += 1
        return False
    elif octopi[row][col] == 9:  # give it some flair and cascade it
        octopi[row][col] = 'X'
    return True


def count_flashes(octopi):
     count = 0
     for row, line in enumerate(octopi):
        for col, char in enumerate(line):
            if octopi[row][col] == 'X':
                count += 1
     return count

def maximum(a, b):
    if a >= b:
        return a
    else:
        return b

def minimum(a, b):
    if a <= b:
        return a
    else:
        return b

def cascade(octopi, row, col):
    width = len(octopi[0])
    depth = len(octopi)
    queue = []
    queue.append([row, col])

    while len(queue) > 0:
        row, col = queue.pop(0)
        increase_power(row, col, octopi)

        # cascade the power to its friends if its flashing
        if octopi[row][col] == 'X':

            # it already was an X or is transformed to an X so cascade to neighbors
            r = maximum(row-1, 0)
            while r <= minimum(row+1, depth-1):
                c = maximum(col-1, 0)
                while c <= minimum(col+1, width-1):
                    if octopi[r][c] != 'X':
                        if increase_power(r,c, octopi): # this one just flashed, so we need to continue the cascade
                            queue.append([r, c])
                    c += 1
                r += 1
