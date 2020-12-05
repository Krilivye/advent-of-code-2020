def read_batch_of_passports(filename):
    all_passports = []
    with open(filename) as batch:
        passports = divide_batch_by_blank_line(batch)
        for passp in passports:
            all_passports.append(Passport(passp))

    return all_passports


class Passport:
    def __init__(self, raw_passport=""):
        self.raw_passport = "".join(raw_passport)

    def analyse(self):
        self._clean()
        return self.passport

    def _clean(self):
        self.passport = "".join(self.raw_passport)
        self.passport = self.passport.split(" ")

    def get_fields_values(self):
        f_v = dict()
        for data in self.analyse():
            related = data.strip().splitlines()
            for elem in related:
                field, value = elem.split(":")
                f_v[field] = value
        return f_v

    def is_valid(self):
        # if not self.check_mandatory_fiels():
        # return False
        # return True

        f_v = self.get_fields_values()

        if len(set(f_v.keys())) == 7:
            if not (
                set(f_v.keys())
                == set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
            ):
                return False
        if len(set(f_v.keys())) == 8:
            if not (
                set(f_v.keys())
                == set(
                    ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
                )
            ):
                return False
        if not (7 <= len(set(f_v.keys())) <= 8):
            return False

        birth_year = f_v["byr"]
        if not (len(birth_year) == 4):
            return False
        if not (1920 <= int(birth_year) <= 2002):
            return False

        issue_year = f_v["iyr"]
        if not (len(issue_year) == 4):
            return False
        if not (2010 <= int(issue_year) <= 2020):
            return False

        expiration_year = f_v["eyr"]
        if not (len(expiration_year) == 4):
            return False
        if not (2020 <= int(expiration_year) <= 2030):
            return False

        height = f_v["hgt"]
        if "cm" in height:
            if not (150 <= int(height[:-2]) <= 193):
                return False
        if "in" in height:
            if not (59 <= int(height[:-2]) <= 76):
                return False
        if not ("cm" in height or "in" in height):
            return False

        hair_color = f_v["hcl"]
        if hair_color[0] != "#":
            return False
        if not len(hair_color[1:]) == 6:
            return False
        for l in hair_color[1:]:
            if l not in [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
            ]:
                return False

        eye_color = f_v["ecl"]
        if eye_color not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        pid = f_v["pid"]
        if not len(pid) == 9:
            return False
        if not pid.isdigit():
            return False
        return True

    def check_mandatory_fiels(self):
        mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for field in mandatory_fields:
            if field not in self.raw_passport:
                return False
        return True


def divide_batch_by_blank_line(filefeeder):
    passports = []
    a_passport = []
    for line in filefeeder:
        if not line.strip():
            passports.append(a_passport)
            a_passport = []
            continue
        a_passport.append(line)
    passports.append(a_passport)
    return passports


def count_valid_passports_in(passports):
    return len(list(filter(lambda x: x.is_valid(), passports)))


if __name__ == "__main__":
    passports = read_batch_of_passports("input_day4.txt")
    print(len(passports))
    print(count_valid_passports_in(passports))

    passports = read_batch_of_passports("bad.txt")
    # print(count_valid_passports_in(passports))

    passports = read_batch_of_passports("good.txt")
    # print(count_valid_passports_in(passports))
