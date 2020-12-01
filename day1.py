from itertools import combinations
from math import prod


class ExpenseReport:
    def __init__(self):
        self.list_of_expense = []

    def get_all_expenses_from_file(self, filename):
        with open(filename) as expense_report:
            for line in expense_report:
                self.list_of_expense.append(int(line))

    def find_n_entries_that_sum_to(self, n, target):
        tuples_of_entries = combinations(self.list_of_expense, n)

        def condition(tuples_of_entries):
            return sum(tuples_of_entries) == target

        return next(filter(condition, tuples_of_entries))


if __name__ == "__main__":
    expense_report = ExpenseReport()
    expense_report.get_all_expenses_from_file("expense_report.txt")
    target = 2020
    two_entries = expense_report.find_n_entries_that_sum_to(2, target)

    print(
        f"""In this list, the two entries that sum to {target} are {two_entries[0]} and {two_entries[1]}.
Multiplying theme together produces {two_entries[0]} * {two_entries[1]} = {prod(two_entries)}, so the correct 
 answer is {prod(two_entries)}"""
    )

    three_entries = expense_report.find_n_entries_that_sum_to(3, target)
    print(
        f"""The product of the three entries that sum to {target} is
{prod(three_entries)}"""
    )
