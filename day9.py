# coding=utf-8
# Advent of Code 2021 - Day 9
import utils, sys, csv
import submarine

def main_day9():
    sub = submarine.Submarine()

    points = utils.read_file("./data/heightmap.csv", "field", '|')
    x = {"min": 0, "max": len(points[0])}
    y = {"min": 0, "max": len(points)}

    low = {}
    risk_level = 0
    basin = []
    for row in range(y["min"], y["max"]):
        for col in range(x["min"], x["max"]):
            up = (row == y["min"] or (int(points[row][col]) < int(points[row-1][col])))
            down = (row == y["max"]-1 or (int(points[row][col]) < int(points[row+1][col])))
            left = (col == x["min"] or (int(points[row][col]) < int(points[row][col-1])))
            right = (col == x["max"]-1 or (int(points[row][col]) < int(points[row][col+1])))

            # record the point
            if up and down and left and right:
                risk_level += 1 + int(points[row][col])

                # calculate the basin size
                size = walk_basin(x, y, points, row, col)
                basin.append(size)

    print "RISK LEVEL"
    print '  Risk = {0}'.format(risk_level) # 491


    basin.sort(reverse=True)
    print "\nBASIN SIZES"
    print '  Size = {0}'.format(basin[0] * basin[1] * basin[2]) # 1075536



# pass in the low point then walk the basin
def walk_basin(x, y, points, row, col):
    visited = []
    queue = []
    queue.append([row,col]) # add the original point

    while len(queue) > 0:
        row, col = queue.pop(0)
        if [row,col] in visited: # shouldn't happen
            continue

        if int(points[row][col]) == 9: # stop going this direction
            continue

        # count this one then check its neighbors
        visited.append([row,col]) # count it

        # add its neighbors
        if y["min"] < row-1 < y["max"]:
            if [row - 1,col] not in visited and [row-1,col] not in queue and points[row-1][col] != 9:
                queue.append([row - 1,col])

        if y["min"] <= row+1 < y["max"]:
            if [row + 1, col] not in visited and [row + 1, col] not in queue and points[row+1][col] != 9:
                queue.append([row + 1, col])

        if x["min"] < col-1 < x["max"]:
            if [row,col-1] not in visited and [row,col-1] not in queue and points[row][col-1] != 9:
                queue.append([row,col - 1])

        if x["min"] <= col+1 < x["max"]:
            if [row, col + 1] not in visited and [row, col + 1] not in queue and points[row][col+1] != 9:
                queue.append([row, col + 1])

    return len(visited)
