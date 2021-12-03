# coding=utf-8
# Advent of Code 2021 - Day 1
import utils
import submarine

def main_day3():
    sub = submarine.Submarine()

    # DAY 3 ----------------------------------------------------------
    print('\n\n***** DAY 2 *****')
    # process location after movement
    diagnostics = utils.read_file("./data/diagnostics.csv", "field", ' ')
    # print(diagnostics)
    diagnostic = sub.determine_power(diagnostics)

    print('\nPower Consumption:\n  Gamma = {0}\n  Epsilon = {1}\n  Power = {2}'
          .format(diagnostic.gamma, diagnostic.epsilon, diagnostic.power_consumption))




