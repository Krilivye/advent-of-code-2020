from day4 import (
    read_batch_of_passports,
    Passport,
    divide_batch_by_blank_line,
    count_valid_passports_in,
)


def test_read_passports():
    # Arrange
    filename = "example.txt"

    # Act
    batch_of_passports = read_batch_of_passports(filename)

    assert len(batch_of_passports) == 4
    first_passport = batch_of_passports[0]
    assert type(first_passport) == Passport
    first_passport.raw_passport == """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm"""


def test_divide_batch_by_blank_line():
    # Arrange
    line_with_a_blank = (
        "auiieauie",
        "  \r\n",
        "aaa",
        "bb",
        "   \n   ",
        "yolo",
        "\n",
        "swag",
    )
    # Act
    batch_of_passports = divide_batch_by_blank_line(line_with_a_blank)

    # Assert
    assert len(batch_of_passports) == 4


def test_analyse_passport():
    raw_passport = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
 byr:1937 iyr:2017 cid:147 hgt:183cm"""
    first_passport = Passport(raw_passport)

    passport_fields = first_passport.analyse()

    assert len(passport_fields) == 8


def test_valid_passport():
    raw_passport = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
 byr:1937 iyr:2017 cid:147 hgt:183cm"""
    first_passport = Passport(raw_passport)

    assert first_passport.is_valid()


def test_count_valid_passports():
    # Arrange
    filename = "example.txt"
    batch_of_passports = read_batch_of_passports(filename)

    count = count_valid_passports_in(batch_of_passports)

    assert count == 2
