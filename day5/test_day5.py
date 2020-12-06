from day5 import F, B, L, R, decode_a_raw_boarding_pass


def test_F_means_lower_half_of_a_range():
    assert F(range(128)) == range(0, 64)
    assert F(range(32, 64)) == range(32, 48)
    assert F(range(44, 46)) == 44


def test_B_mears_uper_half_of_a_range():
    assert B(range(0, 64)) == range(32, 64)
    assert B(range(32, 48)) == range(40, 48)
    assert B(range(40, 48)) == range(44, 48)
    assert B(range(40, 42)) == 41


def test_LR():
    assert R(range(8)) == range(4, 8)
    assert L(range(4, 8)) == range(4, 6)
    assert R(range(4, 6)) == 5


def test_combination():
    assert F(F(B(B(F(B(F(range(128)))))))) == 44


def test_decode_a_boarding_pass():
    raw_boarding_pass = "FBFBBFFRLR"

    seat = decode_a_raw_boarding_pass(raw_boarding_pass)

    assert seat == 357


def test_somes_boarding_pass():
    first = "BFFFBBFRRR"
    second = "FFFBBBFRRR"
    third = "BBFFBBFRLL"
    seat1 = decode_a_raw_boarding_pass(first)
    seat2 = decode_a_raw_boarding_pass(second)
    seat3 = decode_a_raw_boarding_pass(third)

    assert seat1 == 567
    assert seat2 == 119
    assert seat3 == 820
