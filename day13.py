# coding=utf-8
# Advent of Code 2021 - Day 12
import utils, re, sys, csv
import submarine


def main_day13():
    sub = submarine.Submarine()
    dots, folds = get_data("./data/dots.csv")
    row_max = max([d[1] for d in dots])
    col_max = max([d[0] for d in dots])

    print "**** ORIGINAL *****"
    print "  Count Dots = {0}".format(len(dots))
    print len(folds)

    for f, fold in enumerate(folds):
        dots = fold_paper(fold, dots)

        print "\n***** FOLD {0} *****".format(f + 1)
        print "  Count Dots = {0}".format(len(dots))

        if len(folds)  == f+1:
            if fold[0] == "y":
                row_max = fold[1]-1
                print_dots(dots, row_max, col_max)
            else:
                col_max = fold[1]-1
                print_dots(dots, row_max, col_max)

def fold_paper(fold, dots):
    fold_dots = set()

    if fold[0] == 'x':
        for dot in dots:
            if dot[0] > fold[1]:
                fold_dots.add((fold[1] - (dot[0] - fold[1]), dot[1]))
            else:
                fold_dots.add(dot)

    if fold[0] == 'y':
        for dot in dots:
            if dot[1] > fold[1]:
                fold_dots.add((dot[0], fold[1] - (dot[1] - fold[1])))
            else:
                fold_dots.add(dot)

    return fold_dots


def print_dots(dots, row_max, col_max):
    # print row_max, col_max

    for r in range(row_max+1):
        for c in range(col_max+1):
            if (c,r) in dots:
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        sys.stdout.write("\n")

def get_data(filename):
    with open(filename) as file:
        rows = file.read().splitlines()

    dots = set()
    folds = []
    for r, row in enumerate(rows):
        if not row.strip():
            break
        dots.add(tuple(map(int, row.split(","))))

    # relies on us knowing the format of the file. could bulletproof this later
    for row in rows[r+1:]:
        fold = row.split('=')
        axis, position = fold[0], fold[1]
        folds.append((axis[-1], int(position)))

    return dots, folds