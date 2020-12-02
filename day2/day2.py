def read(filename):
    with open(filename) as corporate_policies_and_passwords:
        return ParseTheOpenedInput(list(corporate_policies_and_passwords))


class ParseTheOpenedInput:
    def __init__(self, corporate_policies_and_passwords):
        self.corporate_policies_and_passwords = (
            corporate_policies_and_passwords
        )

    def of(self, CorporatePolicyClass, PasswordClass):
        list_of_corporate_policies_and_passwords = []
        for line in self.corporate_policies_and_passwords:
            raw_corp_poly, raw_password = line.split(":")

            corp_poly = CorporatePolicyClass(raw_corp_poly)
            password = PasswordClass(raw_password)
            list_of_corporate_policies_and_passwords.append(
                (corp_poly, password)
            )
        return list_of_corporate_policies_and_passwords


class Password:
    def __init__(self, raw_password):
        self.password = raw_password.strip()  ### le strip qui vous perdra!

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

    def __str__(self):
        return f"""{self.raw_corp_policy} means that the password must contain {self.letter_to_find} at least {self.lowest_time} time and at most {self.highest_time} time"""


class OfficialToboganCorporatePolicy:
    def __init__(self, raw_corp_policy):
        self.raw_corp_policy = raw_corp_policy
        self._deconstruct(raw_corp_policy)

    def match(self, password: str):
        if (
            password[self.first_position] == self.letter_to_find
            and password[self.second_position] == self.letter_to_find
        ):
            return False
        if password[self.first_position] == self.letter_to_find:
            return True
        if password[self.second_position] == self.letter_to_find:
            return True
        return False

    def _deconstruct(self, raw_corp_policy):
        first_and_second_position, letter_to_find = raw_corp_policy.split(" ")
        (
            raw_first_position,
            raw_second_position,
        ) = first_and_second_position.split("-")
        self.letter_to_find = letter_to_find
        self.first_position = int(raw_first_position) - 1
        self.second_position = int(raw_second_position) - 1

    def __str__(self):
        return f"""{self.raw_corp_policy} means that the password must contain the {self.letter_to_find} in the {self.first_position} position or in the {self.second_position} position"""


def password_validate_their_policy(password_and_its_policy):
    corporate_policy, password = password_and_its_policy
    return password.validate(corporate_policy)


def how_many(validation_function, list_of_passwords_and_policies):
    return len(
        list(filter(validation_function, list_of_passwords_and_policies))
    )


if __name__ == "__main__":

    in_this_list = read("puzzle_input_day2.txt")

    print(
        how_many(
            password_validate_their_policy,
            in_this_list.of(CorporatePolicy, Password),
        )
    )

    print(
        how_many(
            password_validate_their_policy,
            in_this_list.of(OfficialToboganCorporatePolicy, Password),
        )
    )
