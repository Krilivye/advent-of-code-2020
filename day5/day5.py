import functools
import itertools


def half_a_range_size(a_range) -> int:
    return int(len(a_range) / 2)


def final_lower(a_range):
    if len(a_range) == 1:
        return a_range.start
    return a_range


def final_upper(a_range):
    if len(a_range) == 1:
        return a_range.stop - 1
    return a_range


def lower_half(a_range):
    return range(a_range.start, half_a_range_size(a_range) + a_range.start)


def upper_half(a_range):
    return range(half_a_range_size(a_range) + a_range.start, a_range.stop)


def F(a_range):
    return final_lower(lower_half(a_range))


def B(a_range):
    return final_upper(upper_half(a_range))


def R(a_range):
    return final_upper(upper_half(a_range))


def L(a_range):
    return final_lower(lower_half(a_range))


def string_to_functions(a_string):
    mapping = {"F": F, "B": B, "L": L, "R": R}
    return [mapping[char] for char in a_string.strip()]


def row(boarding_pass):
    return decode(boarding_pass[:7], range(128))


def column(boarding_pass):
    return decode(boarding_pass[-3:], range(8))


def id(boarding_pass):
    return row(boarding_pass) * 8 + column(boarding_pass)


def decode(boarding_pass, a_range):
    return functools.reduce(
        lambda val, function: function(val), boarding_pass, a_range
    )


def boarding_pass_id(boarding_pass):
    return id(boarding_pass)


def decode_a_raw_boarding_pass(raw_boarding_pass):
    boarding_pass = string_to_functions(raw_boarding_pass)
    return id(boarding_pass)


def read(filename):
    with open(filename) as boarding_passes:
        return list(map(decode_a_raw_boarding_pass, boarding_passes))


def highest_seat_id(list_of_seats_ids):
    return max(list_of_seats_ids)


def our_seat(list_of_seats):
    sorted_seat = sorted(list_of_seats)
    for i, s in enumerate(sorted_seat):
        if s + 1 != sorted_seat[i + 1]:
            return s + 1


def of_all_the_ids_from(an_iterator):
    return map(decode_a_raw_boarding_pass, an_iterator)


def main(filename):
    with open(filename) as boarding_passes:
        data_for_question_1, data_for_question_2 = itertools.tee(
            boarding_passes
        )
        print(highest_seat_id(of_all_the_ids_from(data_for_question_1)))
        print(our_seat(of_all_the_ids_from(data_for_question_2)))


if __name__ == "__main__":
    main("puzzle_input.txt")
