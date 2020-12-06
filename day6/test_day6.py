example = ("abcx", "abcy", "abcz")


def read_a_group(group):

    list_of_questions = []

    for people in group:
        list_of_questions.append(list(people))
    return list_of_questions


def common_in_group(group):
    set_of_question = set()
    for question in group:
        set_of_question.update(question)
    return set_of_question


def same_in_group(group):
    init = set(group[0])
    for question in group[1:]:
        init = init & set(question)
    return init


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

    print(sum([len(common_in_group(group)) for group in all_groups]))
    print(sum([len(same_in_group(group)) for group in all_groups]))
