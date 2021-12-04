# coding=utf-8
# Advent of Code 2021 - Submarine Location
import utils

class Location:
    def __init__(self, forward, depth):
        self.forward = forward
        self.depth = depth

    # Determine the Location
    def determine_location(self, movement):
        for direction, units in movement:
            if direction == "up":
                self.depth -= int(units)
            elif direction == "down":
                self.depth += int(units)
            else:
                self.forward += int(units)

