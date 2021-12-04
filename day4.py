# coding=utf-8
# Advent of Code 2021 - Day 4
import utils, sys
import submarine
import bingo

def main_day4():
    sub = submarine.Submarine()

    ## Let's load the Bingo Boards so that we can play with the Octopus!
    sub.bingo = bingo.Bingo(utils.read_file("./data/bingo_calls.csv", "row", ','),
                            utils.read_grid_file("./data/bingo_boards.csv", "field", ','))

    # print(sub.bingo.calls)
    # print(len(sub.bingo.boards), sub.bingo.boards)
    # print(len(sub.bingo.status), sub.bingo.status)

    # process the calls for all boards
    winners = 0
    for call in sub.bingo.calls:
        for b, board in enumerate(sub.bingo.boards):

            # get the tracker for the Board and only continue of this board hasn't already won
            board_status = sub.bingo.status[b]
            tracker = sub.bingo.trackers[b]
            if tracker.is_winner():
                continue

            for row, row_status in zip(board, board_status):
                if call in row:
                    row_status[row.index(call)] = True
                    tracker.increment(board.index(row), row.index(call), row[row.index(call)])

                    ## every time we mark a winner, check to see if the board has won
                    if tracker.is_winner():
                        winners += 1

                        # first winner
                        if winners == 1:
                            print ('First Winning Board Score')
                            print (' Board = {0}\n Unmarked = {1}\n Last Call = {2}\n Final Score = {3}'.format(b+1,
                                                                                                               tracker.score,
                                                                                                               call,
                                                                                                               tracker.score * call)) # 45031
                        # last winner
                        if winners == len(sub.bingo.boards):
                            print ('\n\nLast Winning Board Score')
                            print (' Board = {0}\n Unmarked = {1}\n Last Call = {2}\n Final Score = {3}'.format(b+1,
                                                                                                               tracker.score,
                                                                                                               call,
                                                                                                               tracker.score * call)) # 2568




