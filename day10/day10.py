from collections import Counter


def get_data():
    with open("puzzle_input.txt") as puzzle:
        return [int(adapters.strip()) for adapters in puzzle]


if __name__ == "__main__":
    bag = get_data()
    maxi = max(bag)
    adapters = sorted(bag)
    outlet = 0
    one = 0
    three = 0
    for i, value in enumerate(adapters):
        if value == outlet + 1:
            one += 1
        if value == outlet + 3:
            three += 1
        outlet = value

    print(one * (three + 1))

    solutions = Counter()
    solutions[0] = 1
    for adapter in adapters:
        solutions[adapter] = (
            solutions[adapter - 1]
            + solutions[adapter - 2]
            + solutions[adapter - 3]
        )

    print(solutions[max(adapters)])
