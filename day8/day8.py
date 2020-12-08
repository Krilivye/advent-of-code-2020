class Instruction:
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = int(argument)
        self.runned = False

    def apply(self, acc, index):
        if self.operation == "acc":
            acc += self.argument
            index += 1
        if self.operation == "jmp":
            index += self.argument
        if self.operation == "nop":
            index += 1

        return acc, index


def get_all_instructions():
    with open("puzzle_input.txt") as puzzle:
        return [Instruction(*line.split()) for line in puzzle]


def run_instructions(intructions):
    running = True
    index = 0
    acc = 0
    while running:
        if index == len(intructions):
            return acc, index
        current_instruction = intructions[index]
        if current_instruction.runned:
            return acc, index

        current_instruction.runned = True
        acc, index = current_instruction.apply(acc, index)


def switch(instruction: Instruction) -> Instruction:
    if instruction.operation == "jmp":
        return Instruction("nop", instruction.argument)
    if instruction.operation == "nop":
        return Instruction("jmp", instruction.argument)
    return instruction


def reset(instructions):
    for instruction in instructions:
        instruction.runned = False
    return instructions


def switch_one_at(instructions, index):
    modified_list = instructions[:]
    modified_list[index] = switch(instructions[index])
    return modified_list


def try_all_solution(instructions):
    for i in range(len(instructions) - 1):
        new_list_of_commands = reset(switch_one_at(instructions, i))
        acc, index = run_instructions(new_list_of_commands)
        if index == len(instructions):
            return (acc, index)


if __name__ == "__main__":
    instructions = get_all_instructions()
    print(run_instructions(instructions))

    print(try_all_solution(instructions))
