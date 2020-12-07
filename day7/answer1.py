with open("puzzle_input.txt") as puzzle:
    a = list(puzzle)
    master = set()

    def bag_of_bags(bags):
        parents = []
        for bag in bags:
            bag_color = bag.split(" bags contain ")[0]
            for g in a:
                if bag_color in g:
                    if not g.startswith(bag_color):
                        parents.append(g)
        master.update(parents)
        return parents

    bags = ["shiny gold"]
    while len(bags) != 0:
        bags = bag_of_bags(bags)
    print(len(master))
