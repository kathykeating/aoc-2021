# coding=utf-8
# Advent of Code 2021 - Day 1
import utils

class Aim:
    def __init__(self):
        self.forward = 0
        self.depth = 0
        self.aim = 0

    # Determine the Location with aim

    def determine_aim(self, movement):
        for direction, units in movement:
            if direction == "up":
                self.aim -= int(units)
            elif direction == "down":
                self.aim += int(units)
            else:
                self.forward += int(units)
                self.depth += int(units) * self.aim