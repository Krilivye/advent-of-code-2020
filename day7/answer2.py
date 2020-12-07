with open("puzzle_input.txt") as f:
    data = list(f)

all_bags = {}

for line in data:

    main_bag, others = line.strip().split(" bags contain ")
    inside_main_bag = []
    bags_in_main_bag = others.split(", ")
    for each_bag in bags_in_main_bag:
        description = each_bag.split(" bag")[0]
        number_of_bags = description[0]
        type_of_bags = description[2:]
        if number_of_bags != "n":  # no other
            inside_main_bag.append((type_of_bags, int(number_of_bags)))
    all_bags[main_bag] = inside_main_bag


bags_count_dict = {}


def count_bags_in(bag):
    bags_count = 0
    for type_of_bags, number_of_bags in all_bags[bag]:
        bags_count += number_of_bags + number_of_bags * count_bags_in(
            type_of_bags
        )
    return bags_count


print(count_bags_in("shiny gold"))
