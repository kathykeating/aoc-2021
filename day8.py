# coding=utf-8
# Advent of Code 2021 - Day 7
import utils, sys, csv
import submarine
import segment

def main_day8():
    sub = submarine.Submarine()
    control = []
    segs = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    for d, a in zip(segs,
                    ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]):
        control.append(segment.Digit(d, a))

    # calculate each segment
    print "CONTROL\n"
    control = score_digits({"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}, control)
    for i, d in enumerate(control):
        print i, d.characters, d.score


    # process the garbled data
    signals = utils.read_file("./data/displays.csv", "row", '|')
    # print signals
    count = 0
    final_score = 0
    for signal in signals:
        print signal[0], signal[1]
        row = ""

        # Part 1 process the output
        for digit in signal[1].split():
            d = digit.strip() # we care about the second output only
            if segs.count(len(d)) == 1:
                count += 1

        # Part 2
        unique = []
        segments = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0}
        for digit in signal[0].split():
            unique.append(segment.Digit(len(digit), digit))
        unique = score_digits(segments, unique)

        # match each digit to the control so that we know the score
        for digit in unique:
            match_control(digit, control)
            # print digit.digit, digit.characters, digit.score

        # calculate the output
        for digit in signal[1].split():
            score = 0
            d = digit.strip() # we care about the second output only
            for c in d:
                score += segments[c]
            row += str(find_control(score, unique))
        print row
        final_score += int(row)


    print "Count of Unique Digits"
    print ("  Unique = {0}\n".format(count)) # 416

    print "\nFinal Score"
    print ("  Score = {0}\n".format(final_score)) # 1043697

def score_digits(segments, digits):
    for digit in digits:
        for c in digit.characters:
            segments[c] += 1

    for i, digit in enumerate(digits):
        for c in digit.characters:
            digit.score += segments[c]

    return digits

def match_control(digit, control):
    for i, d in enumerate(control):
        if d.score == digit.score:
            digit.digit = i
            break

def find_control(score, control):
    for i, d in enumerate(control):
        if d.score == score:
            return d.digit
    return -1