# coding=utf-8
# Advent of Code 2021 - Day 14
import utils, sys
from collections import defaultdict, Counter

SEPARATOR = " -> "

def main_day14():

    # PART 1 ************************
    template, pairs = get_data(open("./data/polymer.txt"))
    count = iterate(template, pairs, 10)
    print "Polymer Occurrences after 10 Rotations"
    print " Max minus Min = {0}.".format(count) # 2915

    # PART 2 ************************
    template, pairs = get_data(open("./data/polymer.txt"))
    count = iterate(template, pairs, 40)
    print "\nPolymer Occurrences after 40 Rotations"
    print " Max minus Min = {0}.".format(count) # 3353146900153


def get_data(file):
    start = next(file).strip()
    next(file)
    moves = defaultdict(defaultdict)
    for row in file:
        if not row.strip():
            continue
        a, b = row.strip().split(" -> ")
        moves[a] = b
    return start, moves


def iterpairs(s):
    for i in range(len(s) - 1):
        yield s[i : i + 2]

def iterate(start, moves, n):
    chars = Counter(start)
    pairs = Counter(iterpairs(start))

    for _ in range(n):
        newpairs = Counter()
        for pair, n in pairs.items():
            r = moves[pair]
            chars[r] += n
            newpairs[pair[0] + r] += n
            newpairs[r + pair[1]] += n
        pairs = newpairs
    common = chars.most_common()
    return common[0][1] - common[-1][1]



