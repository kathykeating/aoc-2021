# coding=utf-8
# Advent of Code 2021 - Day 5
import utils, sys, csv
import submarine
import vents

def main_day5():
    sub = submarine.Submarine()
    hydro = vents.Vents()

    hydro.read_vents_file("./data/vents.csv", "field", ' ')

    # consider only horizontal and vertical vents
    hydro.create_map(False)
    print('2+ Vent Overlaps (horizontal and vertical only)')
    print '  Overlap = {0}'.format(hydro.count_overlap()) # 8111


    hydro.create_map(True)
    print('\n2+ Vent Overlaps (all)')
    print '  Overlap = {0}'.format(hydro.count_overlap()) # 22088


