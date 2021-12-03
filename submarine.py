# coding=utf-8
# Advent of Code 2021 - Day 1
import utils


class Submarine:
    def __init__(self):
        foobar = 1

    class Location:
      def __init__(self, forward, depth):
        self.forward = forward
        self.depth = depth

    class Aim:
      def __init__(self, forward, depth, aim):
        self.forward = forward
        self.depth = depth
        self.aim = aim

    class Diagnostic:
        def __init__(self):
            self.gamma = ""
            self.epsilon = ""
            self.power_consumption = 0

    # Determine the Location
    def determine_location(self, movement):
        position = self.Location(0,0)
        for direction, units in movement:
            if direction == "up":
                position.depth -= int(units)
            elif direction == "down":
                position.depth += int(units)
            else:
                position.forward += int(units)

        return position

    # Determine the Location with aim
    def determine_aim(self, movement):
        position = self.Aim(0,0,0)
        for direction, units in movement:
            if direction == "up":
                position.aim -= int(units)
            elif direction == "down":
                position.aim += int(units)
            else:
                position.forward += int(units)
                position.depth += int(units) * position.aim

        return position


    # Determine the gamma within the diagnostics
    def determine_power(self, diagnostics):
        diagnostic = self.Diagnostic()

        max = [0] * len(diagnostics[0])
        for idx, reading in enumerate(diagnostics):
            # print(reading, len(reading))
            for l, bit in enumerate(reading):
                if int(reading[l]) == 1:
                    max[l] += 1
                else:
                    max[l] -= 1

        # set the bit
        for idx, bit in enumerate(max):
            if int(bit) >= 0:
                diagnostic.gamma += str(1)
                diagnostic.epsilon += str(0)
            else:
                diagnostic.gamma += str(0)
                diagnostic.epsilon += str(1)

        diagnostic.power_consumption = int(diagnostic.gamma,2) * int(diagnostic.epsilon,2)

        return diagnostic
