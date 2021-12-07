# coding=utf-8
# Advent of Code 2021
import sys, getopt
import day1, day2, day3, day4, day5, day6, day7


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"d:",["runday="])
    except getopt.GetoptError:
        print ('main.py -d <runday>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-d", "--runday") and arg.isdigit():
            eval('day{0}.main_day{0}()'.format(arg))
        else:
            eval('day{0}.main_day{0}()'.format(1))
            eval('day{0}.main_day{0}()'.format(2))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


