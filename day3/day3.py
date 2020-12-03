import sys
from math import prod


def get_land_pattern(filename):
    with open(filename) as pattern:
        lines = []
        for line in pattern:
            lines.append(line.strip())
    return lines


def find_next_point(point, slope):
    # print(point)
    return (point[0] + slope[0], point[1] + slope[1])


def is_tree(point, list_of_line):
    return list_of_line[point[1]][point[0]] == "#"


def get_trees_on_the_slope(slope, list_of_line):
    point = (0, 0)
    count_trees = 0
    height = len(list_of_line)
    width = len(list_of_line[0])

    # print(height, width)
    while point[1] < height:
        if is_tree(point, list_of_line):
            count_trees += 1
        point = find_next_point(point, slope)
        point = adjust_width(point, width)
    return count_trees


def adjust_width(point, width):
    if point[0] >= width:
        point = (point[0] % width, point[1])
    return point


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        slop_to_test = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        trees_in_slopes = [
            get_trees_on_the_slope(slop, get_land_pattern(filename))
            for slop in slop_to_test
        ]
        print("First Part")
        print(
            filename,
            trees_in_slopes[1],
            sep=": ",
        )
        print("Second Part")
        print(
            filename,
            prod(trees_in_slopes),
            sep=": ",
        )
