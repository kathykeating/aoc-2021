# coding=utf-8
# Advent of Code 2021 - Day 12
import utils, sys, csv
import submarine, visits
from collections import defaultdict

START = "start"
END = "end"

def main_day12():
    sub = submarine.Submarine()
    segments = get_data("./data/cave_paths.txt")

    # add each segment to the graph
    graph = defaultdict(list)
    for segment in segments:
        add_segment(graph, segment[0], segment[1])
        # if START not in segment and END not in segment: # also add the reverse
        add_segment(graph, segment[1], segment[0])

    # find the path from Start to End
    path = []
    visit = visits.Visit(1, 0)
    paths = find_path(graph, "start", "end", path, visit)
    print "\nNumber of Valid Paths Visiting Once"
    print " Path Count = {0}".format(len(paths)) # 5756

    path = []
    visit = visits.Visit(2, 0)
    paths = find_path(graph, "start", "end", path, visit)
    print "\nNumber of Valid Paths Visiting One Cave Twice"
    print " Path Count = {0}".format(len(paths)) # 144603



def print_paths(paths):
    for path in paths:
        print path

def find_path(graph, start, end, path, visit):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if is_allowed(path, node, visit):
            newpaths = find_path(graph, node, end, path, visit)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def is_allowed(path, node, visit):
    if node == START or node == END:
        return node not in path

    if node.islower():
        if path.count(node) < 1:  # every lowercase gets at least once
            return True

        if visit.allowed == 1 and path.count(node) >= 1:
            return False

        if visit.allowed == 2:
            if is_max(path, visit.allowed):  # another cave has already been visited more than once
                return False
            else:
                return True
    else:
        return True


def is_max(path, allowed):
    items = defaultdict(list)
    for item in path:
        if item.islower():
            if items.has_key(item):
                items[item] += 1
            else:
                items[item] = 1
            if items[item] == allowed:
                return True
    return False



def add_segment(graph, begin, end):
    graph[begin].append(end)


# process all the routes
def generate_routes(graph):
    routes = []
    for node in graph:
        for neighbor in graph[node]:
            routes.append((node, neighbor))
    return routes


def get_data(filename):
    with open(filename) as file:
        rows = file.read().splitlines()
    data = []
    for row in rows:
        data.append(row.split('-'))
    return data