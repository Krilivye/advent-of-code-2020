example = ("abcx", "abcy", "abcz")


def read_a_group(group):

    set_of_questions = set()

    for people in group:
        set_of_questions.update(list(people))
    return set_of_questions


def divide_batch_by_blank_line(filefeeder):
    groups = []
    a_group = []
    for line in filefeeder:
        if not line.strip():
            groups.append(a_group)
            a_group = []
            continue
        a_group.append(line.strip())
    groups.append(a_group)
    return groups


def read_batch(filename):
    all_groups = []
    with open(filename) as batch:
        groups = divide_batch_by_blank_line(batch)
        for group in groups:
            answers = read_a_group(group)
            all_groups.append(answers)
    return all_groups


if __name__ == "__main__":
    all_groups = read_batch("puzzle_input.txt")

    print(all_groups)
    print(sum([len(group) for group in all_groups]))
