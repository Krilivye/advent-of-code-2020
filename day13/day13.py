from collections import Counter
from copy import deepcopy
from pprint import pprint


def get_instructions(filename):
    with open(filename) as data:
        return [(line[0], int(line[1:].strip())) for line in data]


def first_part(instructions):
    pass


if __name__ == "__main__":
    instructions = get_instructions("test")
    # instructions = get_instructions("input")
    first_part(instructions)
    # second_part(instructions)
