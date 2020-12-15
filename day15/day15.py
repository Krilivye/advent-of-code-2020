from collections import defaultdict
from typing import DefaultDict, Sequence
import array

input = [5, 1, 9, 18, 13, 8, 0]
# input = [0, 3, 6]
turns = 30000000


def optim_array():
    return array.array("L")


def day15(input, turns):
    num_to_speak = input[-1]

    turn_num: DefaultDict[int, Sequence[int]] = defaultdict(optim_array)

    for i, v in enumerate(input):
        turn_num[v].append(i + 1)

    turn = len(input) + 1
    num_to_speak = loop(turn, turns, turn_num, num_to_speak)
    print(num_to_speak)


def loop(
    turn: int,
    turns: int,
    turn_num: DefaultDict[int, Sequence[int]],
    num_to_speak: int,
) -> int:
    while turn <= turns:
        l = len(turn_num[num_to_speak])
        if l > 1:
            num_to_speak = (
                turn_num[num_to_speak][-1] - turn_num[num_to_speak][-2]
            )
            turn_num[num_to_speak].append(turn)
        elif l == 1:
            num_to_speak = 0
            turn_num[num_to_speak].append(turn)
        else:
            num_to_speak = 0
            turn_num[num_to_speak].append(turn)

        turn += 1
    return num_to_speak


day15(input, turns)
