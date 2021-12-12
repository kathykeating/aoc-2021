# coding=utf-8
# Advent of Code 2021 - Day 10
import utils, sys, csv
import submarine

PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"}
SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4 }

def get_data(filename):
    with open(filename) as file:
        return file.read().splitlines()

def main_day10():
    sub = submarine.Submarine()
    first_illegal_score = 0
    incomplete = []
    data = get_data("./data/syntax.txt")
    for  line in data:
        syntax_completion_score = 0
        stack = []
        for char in line:
            if char in PAIRS:
                open = stack.pop()
                if open != PAIRS[char]: # line is corrupted so stop processing this line
                    first_illegal_score += SCORES[char]
                    break
            else:
                stack.append(char)
        else:
            if len(stack) > 0: # line is incomplete, so tally up the additional syntax
                while stack:
                    syntax_completion_score = (syntax_completion_score * 5) + SCORES[stack.pop()]
                incomplete.append(syntax_completion_score)


    print "First Illegal Syntax"
    print " Score = {0}".format(first_illegal_score) # 296535

    incomplete.sort()
    print "\nSyntax Completion Score"
    print" Score = {0}".format(incomplete[len(incomplete)/2]) # 4245130838
