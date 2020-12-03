import sys
from math import prod


def get_land_pattern(filename):
    with open(filename) as pattern:
        return list(map(lambda x: x.strip(), pattern))


def find_next_point(point, slope):
    return (point[0] + slope[0], point[1] + slope[1])


def is_tree(point, pattern):
    return pattern[point[1]][point[0]] == "#"


def get_trees_on_the_slope(slope, pattern):

    return len(
        list(
            filter(
                lambda x: is_tree(x, pattern),
                get_points_of_the_slope(slope, pattern),
            )
        )
    )
    # count = 0
    # for point in get_points_of_the_slope(slope, pattern):
    # if is_tree(point, pattern):
    # count += 1
    # return count


def get_points_of_the_slope(slope, pattern):
    point = (0, 0)
    height = len(pattern)
    width = len(pattern[0])
    while point[1] < height:
        yield point
        point = find_next_point(point, slope)
        point = adjust_width(point, width)


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
