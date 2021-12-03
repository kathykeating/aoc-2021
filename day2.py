# coding=utf-8
# Advent of Code 2021 - Day 1
import utils
import submarine


def main_day2():
    sub = submarine.Submarine()

    # DAY 2 ----------------------------------------------------------
    print('\n\n***** DAY 2 *****')
    # process location after movement
    moves = utils.read_file("./data/movement.csv", "row", ' ')
    # print(moves)

    # calculate location
    location = sub.determine_location(moves)
    print('Location:\n  Forward = {0}\n  Depth = {1}\n  Combined = {2}'
          .format(location.forward, location.depth, location.forward * location.depth)) # 1524750

    # calculate aim
    aim = sub.determine_aim(moves)
    print('\nLocation with Aim:\n  Forward = {0}\n  Depth = {1}\n  Combined = {2}'
          .format(aim.forward, aim.depth, aim.forward * aim.depth))  # 1592426537

