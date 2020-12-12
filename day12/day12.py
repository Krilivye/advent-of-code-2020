from collections import Counter
from copy import deepcopy

from pprint import pprint


def get_instructions(filename):
    with open(filename) as data:
        return [(line[0], int(line[1:].strip())) for line in data]


NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"

n = 0
s = 180
e = 90
w = 270

rose = {0: NORTH, 90: EAST, 180: SOUTH, 270: WEST}
dir_rose = {NORTH: 0, EAST: 90, SOUTH: 180, WEST: 270}


def calulate_new_dir_left(current_dir, value):
    dir_value = (dir_rose[current_dir] - value) % 360
    return rose[dir_value]


def calulate_new_dir_right(current_dir, value):
    dir_value = (dir_rose[current_dir] + value) % 360
    return rose[dir_value]


def calulate_new_waypoint_left(waypoint, value):
    new_waypoint = {NORTH: 0, SOUTH: 0, EAST: 0, WEST: 0}
    for key, val in waypoint.items():
        new_dir = calulate_new_dir_left(key, value)
        new_waypoint[new_dir] = val
    return new_waypoint


def calulate_new_waypoint_right(waypoint, value):
    new_waypoint = {NORTH: 0, SOUTH: 0, EAST: 0, WEST: 0}
    for key, val in waypoint.items():
        new_dir = calulate_new_dir_right(key, value)
        new_waypoint[new_dir] = val
    return new_waypoint


def zeroing(values, dir1, dir2):
    if values[dir1] >= values[dir2]:
        values[dir1] = values[dir1] - values[dir2]
        values[dir2] = 0


def calculate_position(values):
    zeroing(values, NORTH, SOUTH)
    zeroing(values, SOUTH, NORTH)
    zeroing(values, EAST, WEST)
    zeroing(values, WEST, EAST)
    return values


def first_part(instructions):
    values = {NORTH: 0, SOUTH: 0, EAST: 0, WEST: 0}

    current_dir = EAST
    for dir, value in instructions:
        if dir == NORTH:
            values[NORTH] += value
        if dir == SOUTH:
            values[SOUTH] += value
        if dir == EAST:
            values[EAST] += value
        if dir == WEST:
            values[WEST] += value
        if dir == LEFT:
            current_dir = calulate_new_dir_left(current_dir, value)
        if dir == RIGHT:
            current_dir = calulate_new_dir_right(current_dir, value)
        if dir == FORWARD:
            values[current_dir] += value

    position = calculate_position(values)
    pprint(sum(position.values()))


def second_part(instructions):

    waypoint = {NORTH: 1, SOUTH: 0, EAST: 10, WEST: 0}
    ship = {NORTH: 1, SOUTH: 1, EAST: 1, WEST: 1}
    for dir, value in instructions:
        if dir == NORTH:
            waypoint[NORTH] += value
        if dir == SOUTH:
            waypoint[SOUTH] += value
        if dir == EAST:
            waypoint[EAST] += value
        if dir == WEST:
            waypoint[WEST] += value
        if dir == LEFT:
            waypoint = calulate_new_waypoint_left(waypoint, value)
        if dir == RIGHT:
            waypoint = calulate_new_waypoint_right(waypoint, value)
        if dir == FORWARD:
            for key, val in ship.items():
                ship[key] = ship[key] + waypoint[key] * value
            ship = calculate_position(ship)
        waypoint = calculate_position(waypoint)
    pprint(sum(ship.values()))


if __name__ == "__main__":
    instructions = get_instructions("input")
    # instructions = get_instructions("input")
    first_part(instructions)
    second_part(instructions)
