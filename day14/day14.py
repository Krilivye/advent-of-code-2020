from collections import Counter
from copy import deepcopy

from pprint import pprint
from typing import List
import re


def get_instructions(filename):
    with open(filename) as data:
        return [line.strip() for line in data]


def parse_line(line: str, current_mask: str):
    key, value = line.split(" = ")
    index = None
    if line.startswith("mask"):
        current_mask = value
    if line.startswith("mem"):
        index = int(key[4:-1])
        value = int(value)
    return current_mask, index, value


def first_part(instructions):
    memory = {}
    current_mask = None
    for line in instructions:
        current_mask, index, value = parse_line(line, current_mask)
        if index:
            bin_value = list(convert_int_to_bin32(value))
            new_value = [0] * 36

            for i, (bit_mask, value) in enumerate(
                zip(current_mask, bin_value)
            ):
                if bit_mask == "X":
                    new_value[i] = value
                else:
                    new_value[i] = bit_mask

            memory[index] = int("".join(new_value), 2)
    print(sum(memory.values()))


def convert_int_to_bin32(i: int):
    return bin(i)[2:].zfill(36)


def second_part(instructions):
    memory = {}
    current_mask = None
    for line in instructions:
        current_mask, index, value = parse_line(line, current_mask)

        if index:
            bin_add = list(convert_int_to_bin32(index))
            address_mask = ["0"] * 36

            for i, (bit_mask, bit_value) in enumerate(
                zip(current_mask, bin_add)
            ):
                if bit_mask == "X":
                    address_mask[i] = "X"
                elif bit_mask == "0":
                    address_mask[i] = bit_value
                elif bit_mask == "1":
                    address_mask[i] = "1"

            address_mask = "".join(address_mask)

            number_of_bit_to_change = address_mask.count("X")

            all_floating_bits = []
            for i in range(2 ** number_of_bit_to_change):
                all_floating_bits.append(
                    list(bin(i)[2:].zfill(number_of_bit_to_change))
                )

            for floating_bits in all_floating_bits:
                new_address = ""
                for bit_mask in address_mask:
                    if bit_mask != "X":
                        new_address += str(bit_mask)
                    else:
                        new_address += str(floating_bits.pop())
                memory[int(new_address, 2)] = value

    print(sum(memory.values()))


if __name__ == "__main__":
    instructions = get_instructions("input")
    # instructions = get_instructions("test")
    first_part(instructions)
    second_part(instructions)
