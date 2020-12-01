from itertools import combinations
from math import prod


def read(filename):
    list_of_expense = []
    with open(filename) as expense_report:
        for line in expense_report:
            list_of_expense.append(int(line))
    return ExpenseReport(list_of_expense)


class ExpenseReport:
    def __init__(self, list_of_expense):
        self.list_of_expense = list_of_expense

    def find_the(self, number):
        return Entries(combinations(self.list_of_expense, number))


class Entries:
    def __init__(self, entries):
        self.entries = entries

    def entries_that_sum_to(self, number):
        def condition(entries):
            return sum(entries) == number

        return SelectedEntries(next(filter(condition, self.entries)))


class SelectedEntries:
    def __init__(self, selected_entries):
        self.selected_entries = selected_entries

    def and_multiply_them_together(self):
        return prod(self.selected_entries)


if __name__ == "__main__":
    in_this_list = read("expense_report.txt")
    print(
        in_this_list.find_the(2)
        .entries_that_sum_to(2020)
        .and_multiply_them_together()
    )
    print(
        in_this_list.find_the(3)
        .entries_that_sum_to(2020)
        .and_multiply_them_together()
    )
