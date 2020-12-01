class ExpenseReport:
    def __init__(self):
        self.list_of_expense = []

    def read_the_expense_report(self):
        with open("expense_report.txt") as expense_report:
            for line in expense_report:
                self.list_of_expense.append(int(line))

    def find_the_two_entries_that_sum_to(self, target=2020):
        for i in self.list_of_expense:
            if target - i in self.list_of_expense:
                return i, target - i

    def what_is_the_product_of_the_three_entries_that_sum_to(
        self, target=2020
    ):
        for i in self.list_of_expense:
            for j in self.list_of_expense:
                for k in self.list_of_expense:
                    if i + j + k == target:
                        return i * j * k


if __name__ == "__main__":
    expense_report = ExpenseReport()
    expense_report.read_the_expense_report()
    target = 2020
    number1, number2 = expense_report.find_the_two_entries_that_sum_to(target)
    multiplyed = number1 * number2

    print(
        f"""In this list, the two entries that sum to {target} are {number1} and {number2}.
Multiplying theme together produces {number1} * {number2} = {multiplyed}, so the correct 
answer is {multiplyed}"""
    )

    three_entries = (
        expense_report.what_is_the_product_of_the_three_entries_that_sum_to(
            target
        )
    )
    print(
        f"""Product of three entries that sum to {target} is {three_entries}"""
    )
