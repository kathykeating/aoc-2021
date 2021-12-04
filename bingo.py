# coding=utf-8
# Advent of Code 2021 - Submarine Location
import utils, sys

class Bingo:
    def __init__(self, calls, boards):
        self.size = 5
        if len(calls) == 1:
            self.calls = [int(x) for x in calls[0]]
        self.boards = boards
        self.status = [[[False for x in range(self.size)] for x in range(self.size)] for y in range(len(boards))]
        self.trackers = [self.Tracker(self.size) for _ in range(len(boards))]
        self.intial_score()

    class Tracker:
        def __init__(self, size):
            self.row_count = [0] * size
            self.column_count = [0] * size
            self.unmarked = size * size
            self.score = 0
            self.winner = False

        def increment(self, r, c, value):
            self.row_count[r] += 1
            self.column_count[c] += 1
            self.unmarked -= 1
            self.score -= value
            if self.row_count[r] == len(self.row_count) or self.column_count[c] == len(self.column_count):
                self.winner = True

        def is_winner(self):
            if self.winner:
                return True
            return False


    def intial_score(self):
        for b, board in enumerate(self.boards):
            score = 0
            for row in board:
                for column in row:
                    score += column

            self.trackers[b].score = score




