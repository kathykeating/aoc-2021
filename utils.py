# coding=utf-8
# Advent of Code 2021 - utilities
import csv

def read_file(file_name, type, delimit):
    f = open(file_name, "r")
    csv_reader = csv.reader(f, delimiter=delimit)

    the_list = []
    for row in csv_reader:
        if type == "row":
            the_list.append(row)
        else:
            the_list.append(row[0])
    return the_list


def read_grid_file(file_name, type, delimit):
    grids = []
    f = open(file_name, "r")
    csv_reader = csv.reader(f, delimiter=delimit)

    grid = []
    for row in csv_reader:
        if row:
            item = str(row[0]).replace('  ', ' ').split()
            grid.append([int(x) for x in item])
        else:
            grids.append(grid) # an empty row separates each grid
            grid = []
    return grids

