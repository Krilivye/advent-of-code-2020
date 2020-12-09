from itertools import combinations
from functools import lru_cache
import sys


def get_data():
    with open("puzzle_input.txt") as puzzle:
        return [int(line.strip()) for line in puzzle]


def get_preamble(data, index, size):
    return data[index : index + size]


def all_values(data, index, size):
    return list(
        map(sum, tuple(combinations(get_preamble(data, index, size), 2)))
    )


def get_bad_guy(data, size):
    for i, value in enumerate(data[size:]):
        if value not in all_values(data, i, size):
            return value


@lru_cache(128)
def get_intermediate_sum(start, target):
    intermedate_sum = []
    for i in data[start:]:
        intermedate_sum.append(i)
        if sum(intermedate_sum) < target:
            continue
        if sum(intermedate_sum) == target:
            return intermedate_sum
        if sum(intermedate_sum) > target:
            start = start + 1
            return get_intermediate_sum(start, target)


if __name__ == "__main__":
    data = get_data()
    size = 25
    bad = get_bad_guy(data, size)

    start = 0
    print(len(data))
    sys.setrecursionlimit(1150)
    inter = get_intermediate_sum(start, bad)
    print(sum([min(inter), max(inter)]))
