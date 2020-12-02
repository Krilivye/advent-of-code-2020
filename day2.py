def read_a_list(filename):
    with open(filename) as corporate_policies_and_passwords:
        list_of_corporate_policies_and_passwords = []
        for line in corporate_policies_and_passwords:
            raw_corp_poly, raw_password = line.split(":")
            corp_poly = CorporatePolicy(raw_corp_poly)
            password = Password(raw_password)
            list_of_corporate_policies_and_passwords.append(
                (corp_poly, password)
            )
        return list_of_corporate_policies_and_passwords


def read_a_list2(filename):
    with open(filename) as corporate_policies_and_passwords:
        list_of_corporate_policies_and_passwords = []
        for line in corporate_policies_and_passwords:
            raw_corp_poly, raw_password = line.split(":")
            corp_poly = ToboganCorporatePolicy(raw_corp_poly)
            password = Password(raw_password)
            list_of_corporate_policies_and_passwords.append(
                (corp_poly, password)
            )
        return list_of_corporate_policies_and_passwords


class Password:
    def __init__(self, password):
        self.password = password.strip()  ### le strip qui vous perdra!

    def validate(self, corp_policy):
        return corp_policy.match(self.password)


class CorporatePolicy:
    def __init__(self, raw_corp_policy):
        self.raw_corp_policy = raw_corp_policy
        self._deconstruct(raw_corp_policy)

    def match(self, password: str):
        return (
            self.lowest_time
            <= password.count(self.letter_to_find)
            <= self.highest_time
        )

    def _deconstruct(self, raw_corp_policy):
        lowest_and_highest_times, letter_to_find = raw_corp_policy.split(" ")
        lowest_time, highest_time = lowest_and_highest_times.split("-")
        self.letter_to_find = letter_to_find
        self.lowest_time = int(lowest_time)
        self.highest_time = int(highest_time)


class ToboganCorporatePolicy:
    def __init__(self, raw_corp_policy):
        self.raw_corp_policy = raw_corp_policy
        self._deconstruct(raw_corp_policy)

    def match(self, password: str):
        if (
            password[self.lowest_time - 1] == self.letter_to_find
            and password[self.highest_time - 1] == self.letter_to_find
        ):
            return False
        if password[self.lowest_time - 1] == self.letter_to_find:
            return True
        if password[self.highest_time - 1] == self.letter_to_find:
            return True
        return False

    def _deconstruct(self, raw_corp_policy):
        lowest_and_highest_times, letter_to_find = raw_corp_policy.split(" ")
        lowest_time, highest_time = lowest_and_highest_times.split("-")
        self.letter_to_find = letter_to_find
        self.lowest_time = int(lowest_time)
        self.highest_time = int(highest_time)


if __name__ == "__main__":
    corporate_policies_and_passwords = read_a_list("puzzle_input_day2.txt")
    valid_password_count = 0
    for corporate_policy, password in corporate_policies_and_passwords:
        if password.validate(corporate_policy):
            valid_password_count += 1
    print(valid_password_count)

    corporate_policies_and_passwords = read_a_list2("puzzle_input_day2.txt")
    valid_password_count = 0
    for corporate_policy, password in corporate_policies_and_passwords:
        if password.validate(corporate_policy):
            valid_password_count += 1
    print(valid_password_count)

    def test_unitaire():
        corp = ToboganCorporatePolicy("1-3 a")
        assert corp.match("abcde") is True
        assert corp.match("cdefg") is False
        assert corp.match("cdafg") is True

        corp = ToboganCorporatePolicy("2-9 c")
        assert corp.match("ccccccccc") is False

    test_unitaire()
