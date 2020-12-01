def read_the_expense_report():
    with open("expense_report.txt") as expense_report:
        list_of_expense = []
        for line in expense_report:
            list_of_expense.append(int(line))
        return list_of_expense


def find_the_two_entries_that_sum_to(list_of_expense, year=2020):
    for i in list_of_expense:
        if year - i in list_of_expense:
            return i, year - i


def what_is_the_product_of_the_three_entries_that_sum_to(
    list_of_expense, year=2020
):
    for i in list_of_expense:
        for j in list_of_expense:
            for k in list_of_expense:
                if i + j + k == year:
                    return i * j * k


if __name__ == "__main__":
    list_of_expense = read_the_expense_report()
    year = 2020
    number1, number2 = find_the_two_entries_that_sum_to(list_of_expense, year)
    multiplyed = number1 * number2

    print(
        f"""In this list, the two entries that sum to {year} are {number1} and {number2}.
Multiplying theme together produces {number1} * {number2} = {multiplyed}, so the correct 
answer is {multiplyed}"""
    )

    three_entries = what_is_the_product_of_the_three_entries_that_sum_to(
        list_of_expense, year
    )
    print(
        f"""Product of three entries that sum to {year} is {three_entries}"""
    )
