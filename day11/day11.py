from collections import Counter
from copy import deepcopy

from pprint import pprint


def get_data():
    with open("input.txt") as data:
        return [line.strip() for line in data]


EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


def count_adjacent_in_line(state, r, c):
    v = [-1, 0, 1]
    h = [-1, 0, 1]
    count = 0
    for i in v:
        for j in h:
            if i == 0 and j == 0:
                continue
            new_r = r + i
            new_j = c + j

            while (
                0 <= new_r < len(state)
                and 0 <= new_j < len(state[0])
                and state[new_r][new_j] is FLOOR
            ):
                new_r = new_r + i
                new_j = new_j + j
            if 0 <= new_r < len(state) and 0 <= new_j < len(state[0]):
                if state[new_r][new_j] is OCCUPIED:
                    count += 1
    return count


def count_adjacent(state, r, c):
    v = [-1, 0, 1]
    h = [-1, 0, 1]
    count = 0
    for i in v:
        for j in h:
            if i == 0 and j == 0:
                continue
            new_r = r + i
            new_j = c + j
            if 0 <= new_r < len(state) and 0 <= new_j < len(state[0]):
                if state[new_r][new_j] is OCCUPIED:
                    count += 1
    return count


def no_adjacent_in_line(state, r, c):
    count = count_adjacent_in_line(state, r, c)
    return count == 0


def no_adjacent(state, r, c):
    count = count_adjacent(state, r, c)
    return count == 0


def four_or_more(state, r, c):
    count = count_adjacent(state, r, c)
    return 4 <= count


def five_or_more(state, r, c):
    count = count_adjacent_in_line(state, r, c)
    return 5 <= count


def next_state(state, previous_state, rules_of_adajcent, rule_of_number):
    for r, line in enumerate(state):
        for c, seat in enumerate(line):
            if seat is EMPTY and rules_of_adajcent(previous_state, r, c):
                state[r] = state[r][0:c] + OCCUPIED + state[r][c + 1 :]
                continue
            if seat is OCCUPIED and rule_of_number(previous_state, r, c):
                state[r] = state[r][0:c] + EMPTY + state[r][c + 1 :]
                continue
    return state


def find_stabilize_state(state, rules_of_adajcent, rule_of_number):
    while True:
        previous_state = deepcopy(state)
        state = next_state(
            state, previous_state, rules_of_adajcent, rule_of_number
        )
        if state == previous_state:
            break
    return state


if __name__ == "__main__":
    state = get_data()

    state = find_stabilize_state(state, no_adjacent, four_or_more)
    print(sum([line.count(OCCUPIED) for line in state]))

    state = get_data()
    state = find_stabilize_state(state, no_adjacent_in_line, five_or_more)
    print(sum([line.count(OCCUPIED) for line in state]))
