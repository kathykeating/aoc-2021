# coding=utf-8
# Advent of Code 2021 - Day 1
import utils


class Diagnostic:
    def __init__(self):
        self.gamma = ""
        self.epsilon = ""
        self.diagnostics = []
        self.max = []

    # load data
    def load_data(self, diagnostics):
        self.diagnostics = diagnostics
        self.max = self.determine_max(diagnostics)

    # calculate the most common digit in each column of the set
    def determine_max(self, list):
        max = [0] * len(list[0])
        ones = [0] * len(list[0])
        zeros = [0] * len(list[0])
        for idx, reading in enumerate(list):
            # print(reading, len(reading))
            for l, bit in enumerate(reading):
                if int(reading[l]) == 1:
                    max[l] += 1
                    ones[l] += 1
                else:
                    max[l] -= 1
                    zeros[l] += 1

        # print("ones=", ones)
        # print("zeros=", zeros)
        return max

    def match_method(self, method, filter):
        # set the match method
        if method == "max":
            match = 0
            if filter >= 0:  # if equal, use one in "max" algorithm
                match = 1
        else:
            match = 1
            if filter >= 0:  # if equal, use zero in "min" algorithm
                match = 0

        return match

    def filter_list(self, list, method, column):
        newlist = []
        filter = self.determine_max(list)
        match = self.match_method(method, filter[column])

        for item in list:
            if int(item[column]) == match:
                newlist.append(item)

        if len(newlist) == 1:
            return newlist
        else:
            return self.filter_list(newlist, method, column + 1)

    # determine the oxygen generator rating from the diagnostics
    def determine_oxygen_generator_rating(self):

        list = self.filter_list(self.diagnostics, "max", 0)
        return int(list[0], 2)

    # determine the CO2 scrubber rating from the diagnostics
    def determine_co2_scrubber_rating(self):

        list = self.filter_list(self.diagnostics, "min", 0)
        return int(list[0], 2)
