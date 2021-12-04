# coding=utf-8
# Advent of Code 2021 - Day 1
import utils
import location
import aim
import diagnostic


class Submarine:
    def __init__(self):
        self.power_consumption = 0
        self.oxygen_generator_rating = 0
        self.co2_scrubber_rating = 0
        self.life_support_rating = 0
        self.location = location.Location(0,0)
        self.aim = aim.Aim()
        self.diagnostic = diagnostic.Diagnostic()


    # Determine the gamma within the diagnostics
    def determine_power(self, diagnostic):
        # set the bit
        for idx, bit in enumerate(diagnostic.max):
            if int(bit) >= 0:
                diagnostic.gamma += str(1)
                diagnostic.epsilon += str(0)
            else:
                diagnostic.gamma += str(0)
                diagnostic.epsilon += str(1)

        self.power_consumption = int(diagnostic.gamma,2) * int(diagnostic.epsilon,2)


