# coding=utf-8
# Advent of Code 2021 - Day 1
import utils
import submarine

def main_day3():
    sub = submarine.Submarine()

    # DAY 3 ----------------------------------------------------------
    print('\n\n***** DAY 3 *****')
    # process determine power consumption
    diagnostics = utils.read_file("./data/diagnostics.csv", "field", ' ')
    diagnostic = sub.Diagnostic(diagnostics)
    sub.determine_power(diagnostic)

    print('\nPower Consumption:\n  Gamma = {0}\n  Epsilon = {1}\n  Power = {2}'
          .format(diagnostic.gamma, diagnostic.epsilon, sub.power_consumption))

    # verify the life support rating determined by the oxygen generator rating
    sub.oxygen_generator_rating = diagnostic.determine_oxygen_generator_rating()
    sub.co2_scrubber_rating = diagnostic.determine_co2_scrubber_rating()
    sub.life_support_rating = sub.oxygen_generator_rating * sub.co2_scrubber_rating

    print('\nLife Support Rating:\n  Oxygen Generator = {0}\n  CO2 Scrubber = {1}\n  Rating = {2}'
          .format(sub.oxygen_generator_rating,
                  sub.co2_scrubber_rating,
                  sub.life_support_rating))