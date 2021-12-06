# coding=utf-8
# Advent of Code 2021 - Day 1
import csv, sys

class Vents:
    def __init__(self):
        self.max_x = 0
        self.max_y = 0
        self.points = []

    def read_vents_file(self, file_name, type, delimit):
        grids = []
        f = open(file_name, "r")
        csv_reader = csv.reader(f, delimiter=delimit)

        for row in csv_reader:
            self.points.append([self.create_point([int(x) for x in row[0].split(',')]),
                           self.create_point([int(x) for x in row[2].split(',')])])


    def create_point(self, point):
        self.max_x = self.max_point(self.max_x, point[0])
        self.max_y = self.max_point(self.max_y, point[1])
        return point

    def max_point(self, current, new):
        if new > current:
            return new
        else:
            return current


    def create_map(self, is_diagonal):
        self.map = [[0 for x in range(self.max_x + 1)] for y in range(self.max_y + 1 )]
        # print "Map Size", self.max_x, self.max_y, len(self.map), len(self.map[0])
        for begin, end in self.points:

            if begin[0] == end[0]: # horizontal
                # print "horizontal", begin, end
                dir = self.direction(begin[1], end[1])
                for y in range(begin[1], end[1]+(1*dir), dir):
                    try:
                        self.map[y][begin[0]] += 1
                    except Exception as e:
                        print "***************************  ERROR: ", e, begin[0], y
                        sys.exit()

            elif begin[1] == end[1]: # vertical
                # print "vertical", begin, end
                dir = self.direction(begin[0], end[0])
                for x in range(begin[0], end[0]+(1*dir), dir):
                    try:
                        self.map[end[1]][x] += 1
                    except Exception as e:
                        print "ERROR: ", e, x, end[1]

            elif is_diagonal: # diagonal
                # print "diagonal", begin, end
                dirx = self.direction(begin[0], end[0])
                diry = self.direction(begin[1], end[1])
                for x, y in zip(range(begin[0], end[0]+(1*dirx), dirx), range(begin[1], end[1]+(1*diry), diry)):
                    self.map[y][x] += 1

        # print "Quality: ", self.map[982][555]


    def count_overlap(self):
        overlap = 0
        for x in range(len(self.map[0])): # width
            for y in range(len(self.map)): # height
                if self.map[y][x] >= 2:
                    overlap += 1

        return overlap


    def direction(self, frm, to):
        if to < frm:
            return -1
        else:
            return 1


