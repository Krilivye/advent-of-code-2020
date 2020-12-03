from math import prod


def get_list_of_lines():
    with open("input_day3.txt") as pattern:
        list_of_line = []
        for line in pattern:
            list_of_line.append(line.strip())
    return list_of_line


def find_next_point(point, slope):
    # print(point)
    return (point[0] + slope[0], point[1] + slope[1])


def is_it_a_tree(point, list_of_line):
    return list_of_line[point[1]][point[0]] == "#"


def check_the_slope(slope, list_of_line):
    point = (0, 0)
    count_trees = 0
    height = len(list_of_line)
    width = len(list_of_line[0])

    # print(height, width)
    for line in list_of_line:
        point = find_next_point(point, slope)
        if point[1] >= height:
            break
        if point[0] >= width:
            point = (point[0] % width, point[1])
        if is_it_a_tree(point, list_of_line):
            count_trees += 1
    return count_trees


slop_to_test = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for slop in slop_to_test:
    check_the_slope(slop, get_list_of_lines())


print(
    prod([check_the_slope(slop, get_list_of_lines()) for slop in slop_to_test])
)
