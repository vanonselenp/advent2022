example_start = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
 2   6   0
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

actual = """            [Q]     [G]     [M]    
            [B] [S] [V]     [P] [R]
    [T]     [C] [F] [L]     [V] [N]
[Q] [P]     [H] [N] [S]     [W] [C]
[F] [G] [B] [J] [B] [N]     [Z] [L]
[L] [Q] [Q] [Z] [M] [Q] [F] [G] [D]
[S] [Z] [M] [G] [H] [C] [C] [H] [Z]
[R] [N] [S] [T] [P] [P] [W] [Q] [G]
 1   2   3   4   5   6   7   8   9 

move 1 from 2 to 6
move 3 from 7 to 9
move 7 from 9 to 4
move 2 from 5 to 3
move 3 from 2 to 8
move 14 from 4 to 5
move 1 from 2 to 1
move 1 from 2 to 3
move 3 from 6 to 8
move 3 from 6 to 9
move 1 from 4 to 6
move 5 from 9 to 8
move 9 from 8 to 9
move 3 from 3 to 8
move 8 from 9 to 4
move 2 from 1 to 7
move 4 from 1 to 5
move 2 from 7 to 1
move 1 from 9 to 6
move 7 from 4 to 7
move 1 from 8 to 4
move 1 from 9 to 8
move 2 from 6 to 7
move 7 from 7 to 3
move 10 from 3 to 1
move 1 from 3 to 2
move 1 from 2 to 9
move 1 from 9 to 8
move 15 from 5 to 8
move 1 from 6 to 9
move 2 from 7 to 3
move 11 from 1 to 8
move 1 from 9 to 8
move 1 from 1 to 5
move 3 from 5 to 2
move 2 from 6 to 9
move 1 from 2 to 4
move 2 from 4 to 5
move 1 from 3 to 6
move 5 from 8 to 3
move 12 from 8 to 4
move 2 from 2 to 5
move 12 from 8 to 1
move 1 from 6 to 9
move 10 from 5 to 7
move 3 from 3 to 9
move 6 from 8 to 9
move 2 from 3 to 5
move 8 from 4 to 7
move 1 from 3 to 2
move 6 from 8 to 6
move 8 from 9 to 3
move 2 from 5 to 4
move 1 from 2 to 3
move 2 from 9 to 2
move 1 from 9 to 2
move 1 from 2 to 1
move 2 from 2 to 4
move 5 from 4 to 2
move 3 from 2 to 3
move 2 from 4 to 2
move 18 from 7 to 3
move 3 from 6 to 9
move 1 from 6 to 3
move 1 from 4 to 1
move 1 from 6 to 3
move 6 from 3 to 9
move 2 from 2 to 6
move 26 from 3 to 7
move 2 from 2 to 3
move 2 from 6 to 8
move 3 from 1 to 5
move 8 from 9 to 1
move 1 from 8 to 5
move 1 from 3 to 1
move 2 from 9 to 3
move 1 from 1 to 2
move 12 from 1 to 7
move 1 from 8 to 5
move 2 from 3 to 5
move 1 from 3 to 6
move 2 from 6 to 2
move 7 from 5 to 7
move 1 from 4 to 2
move 15 from 7 to 4
move 1 from 4 to 9
move 1 from 7 to 6
move 14 from 4 to 2
move 1 from 1 to 2
move 5 from 1 to 5
move 4 from 5 to 4
move 1 from 6 to 3
move 4 from 4 to 7
move 1 from 9 to 2
move 1 from 3 to 5
move 2 from 5 to 1
move 1 from 1 to 6
move 2 from 1 to 5
move 9 from 2 to 9
move 1 from 6 to 1
move 1 from 1 to 9
move 1 from 5 to 4
move 1 from 5 to 6
move 4 from 7 to 2
move 1 from 4 to 1
move 18 from 7 to 1
move 17 from 1 to 7
move 4 from 9 to 5
move 1 from 5 to 8
move 1 from 1 to 4
move 2 from 9 to 6
move 3 from 9 to 7
move 1 from 1 to 5
move 1 from 7 to 5
move 16 from 7 to 2
move 1 from 4 to 2
move 1 from 8 to 7
move 1 from 9 to 8
move 1 from 8 to 4
move 3 from 5 to 3
move 15 from 7 to 6
move 7 from 6 to 4
move 9 from 6 to 2
move 2 from 5 to 7
move 2 from 6 to 8
move 4 from 4 to 7
move 2 from 8 to 1
move 11 from 2 to 7
move 1 from 4 to 2
move 2 from 3 to 6
move 3 from 4 to 5
move 12 from 7 to 1
move 1 from 7 to 3
move 31 from 2 to 4
move 3 from 7 to 2
move 1 from 6 to 3
move 1 from 5 to 1
move 1 from 5 to 2
move 2 from 3 to 4
move 1 from 6 to 1
move 1 from 3 to 6
move 1 from 5 to 6
move 1 from 2 to 4
move 11 from 1 to 4
move 5 from 1 to 5
move 1 from 7 to 3
move 3 from 5 to 8
move 1 from 8 to 7
move 1 from 5 to 3
move 2 from 8 to 5
move 2 from 6 to 2
move 2 from 5 to 1
move 1 from 7 to 9
move 1 from 3 to 9
move 2 from 9 to 5
move 1 from 1 to 6
move 1 from 6 to 5
move 1 from 3 to 5
move 13 from 4 to 8
move 5 from 2 to 3
move 3 from 3 to 4
move 1 from 8 to 6
move 4 from 5 to 2
move 1 from 1 to 5
move 1 from 3 to 7
move 2 from 5 to 4
move 11 from 4 to 5
move 1 from 3 to 7
move 15 from 4 to 2
move 1 from 6 to 4
move 19 from 2 to 8
move 8 from 8 to 3
move 2 from 3 to 8
move 7 from 5 to 4
move 6 from 3 to 4
move 8 from 4 to 5
move 7 from 4 to 6
move 2 from 7 to 5
move 9 from 5 to 6
move 13 from 8 to 3
move 3 from 4 to 3
move 6 from 3 to 4
move 6 from 8 to 2
move 4 from 5 to 9
move 5 from 8 to 7
move 4 from 6 to 2
move 5 from 3 to 5
move 1 from 6 to 9
move 8 from 2 to 6
move 1 from 8 to 7
move 1 from 2 to 5
move 1 from 4 to 1
move 3 from 3 to 1
move 1 from 7 to 3
move 4 from 9 to 8
move 6 from 6 to 2
move 2 from 8 to 4
move 1 from 7 to 6
move 3 from 5 to 1
move 4 from 5 to 3
move 6 from 2 to 9
move 4 from 7 to 4
move 2 from 8 to 5
move 2 from 9 to 5
move 4 from 5 to 6
move 1 from 2 to 5
move 8 from 6 to 7
move 18 from 4 to 2
move 2 from 3 to 6
move 6 from 1 to 8
move 8 from 7 to 9
move 9 from 6 to 4
move 1 from 5 to 4
move 5 from 8 to 4
move 1 from 4 to 5
move 1 from 8 to 1
move 8 from 9 to 8
move 3 from 3 to 9
move 5 from 2 to 7
move 1 from 5 to 2
move 2 from 4 to 8
move 11 from 2 to 8
move 1 from 7 to 2
move 2 from 6 to 5
move 1 from 6 to 2
move 4 from 2 to 3
move 2 from 1 to 3
move 5 from 9 to 7
move 1 from 5 to 8
move 6 from 7 to 8
move 7 from 3 to 7
move 1 from 5 to 9
move 3 from 9 to 7
move 1 from 4 to 1
move 1 from 9 to 8
move 8 from 7 to 3
move 1 from 2 to 4
move 1 from 1 to 7
move 9 from 3 to 7
move 7 from 4 to 7
move 8 from 7 to 3
move 1 from 7 to 9
move 13 from 7 to 4
move 1 from 4 to 6
move 11 from 8 to 2
move 5 from 3 to 7
move 1 from 9 to 6
move 7 from 2 to 9
move 2 from 2 to 4
move 4 from 9 to 2
move 17 from 8 to 3
move 3 from 3 to 4
move 1 from 7 to 6
move 5 from 2 to 3
move 8 from 4 to 1
move 2 from 6 to 4
move 1 from 2 to 7
move 1 from 1 to 4
move 1 from 8 to 2
move 2 from 7 to 4
move 7 from 1 to 9
move 16 from 4 to 2
move 1 from 6 to 1
move 2 from 2 to 9
move 6 from 2 to 7
move 1 from 1 to 6
move 3 from 2 to 6
move 10 from 3 to 6
move 6 from 9 to 8
move 3 from 4 to 3
move 6 from 9 to 2
move 4 from 3 to 7
move 10 from 2 to 5
move 2 from 2 to 6
move 3 from 6 to 3
move 1 from 8 to 2
move 1 from 2 to 6
move 5 from 6 to 1
move 3 from 6 to 7
move 5 from 8 to 4
move 3 from 7 to 1
move 2 from 6 to 1
move 2 from 4 to 1
move 2 from 5 to 8
move 1 from 8 to 7
move 1 from 8 to 9
move 8 from 3 to 4
move 11 from 1 to 7
move 1 from 9 to 8
move 1 from 8 to 3
move 3 from 6 to 3
move 1 from 6 to 8
move 3 from 5 to 2
move 1 from 8 to 6
move 2 from 5 to 8
move 3 from 5 to 6
move 3 from 2 to 4
move 2 from 8 to 4
move 22 from 7 to 3
move 12 from 3 to 2
move 9 from 3 to 9
move 1 from 1 to 2
move 2 from 6 to 8
move 2 from 8 to 4
move 2 from 6 to 5
move 11 from 3 to 1
move 18 from 4 to 3
move 3 from 7 to 3
move 1 from 5 to 7
move 3 from 2 to 4
move 2 from 4 to 9
move 6 from 1 to 4
move 1 from 5 to 1
move 10 from 9 to 3
move 27 from 3 to 9
move 6 from 2 to 8
move 5 from 4 to 2
move 3 from 3 to 8
move 1 from 7 to 8
move 10 from 8 to 2
move 5 from 1 to 5
move 1 from 3 to 5
move 1 from 1 to 8
move 14 from 9 to 4
move 6 from 5 to 6
move 11 from 9 to 4
move 6 from 6 to 3
move 1 from 8 to 6
move 2 from 9 to 5
move 1 from 2 to 5
move 8 from 2 to 1
move 12 from 4 to 7
move 1 from 6 to 8
move 14 from 4 to 1
move 1 from 9 to 8
move 1 from 5 to 1
move 2 from 5 to 2
move 11 from 1 to 6
move 11 from 6 to 1
move 1 from 8 to 7
move 1 from 8 to 2
move 12 from 1 to 7
move 1 from 4 to 7
move 5 from 1 to 5
move 5 from 2 to 6
move 1 from 5 to 6
move 1 from 2 to 9
move 6 from 1 to 3
move 19 from 7 to 2
move 1 from 9 to 6
move 9 from 3 to 2
move 9 from 2 to 7
move 3 from 5 to 8
move 1 from 5 to 1
move 3 from 3 to 9
move 7 from 2 to 9
move 15 from 7 to 2
move 10 from 9 to 4
move 4 from 4 to 9
move 1 from 6 to 4
move 1 from 1 to 6
move 26 from 2 to 5
move 1 from 7 to 3
move 6 from 4 to 8
move 3 from 2 to 9
move 6 from 8 to 3
move 4 from 5 to 7
move 1 from 4 to 5
move 2 from 2 to 1
move 6 from 9 to 1
move 3 from 3 to 8
move 3 from 2 to 8
move 3 from 7 to 9
move 6 from 1 to 7
move 2 from 3 to 2
move 2 from 2 to 5
move 1 from 8 to 6
move 4 from 7 to 3
move 10 from 5 to 3
move 4 from 9 to 1
move 6 from 3 to 1
move 1 from 7 to 4
move 4 from 3 to 2
move 1 from 3 to 1
move 13 from 1 to 5
move 1 from 3 to 7
move 1 from 3 to 8
move 4 from 6 to 3
move 1 from 6 to 3
move 7 from 8 to 2
move 1 from 6 to 9
move 2 from 7 to 2
move 1 from 9 to 5
move 2 from 8 to 6
move 1 from 7 to 5
move 1 from 3 to 1
move 30 from 5 to 2
move 1 from 3 to 4
move 2 from 6 to 1
move 5 from 3 to 4
move 2 from 6 to 5
move 5 from 4 to 3
move 1 from 3 to 1
move 4 from 1 to 6
move 1 from 2 to 5
move 2 from 4 to 9
move 4 from 3 to 5
move 1 from 3 to 5
move 1 from 5 to 3
move 6 from 5 to 1
move 2 from 1 to 9
move 4 from 6 to 2
move 1 from 3 to 5
move 1 from 5 to 2
move 1 from 5 to 2
move 8 from 2 to 5
move 4 from 9 to 6
move 3 from 1 to 4
move 3 from 6 to 2
move 2 from 4 to 2
move 1 from 6 to 1
move 1 from 4 to 6
move 2 from 5 to 1
move 1 from 6 to 8
move 3 from 5 to 2
move 2 from 5 to 6
move 1 from 6 to 7
move 1 from 5 to 9
move 1 from 7 to 5
move 3 from 1 to 9
move 3 from 9 to 5
move 31 from 2 to 6
move 1 from 1 to 3
move 1 from 8 to 9
move 30 from 6 to 9
move 2 from 9 to 8
move 13 from 2 to 3
move 4 from 5 to 2
move 1 from 8 to 4
move 1 from 4 to 1
move 1 from 1 to 6
move 5 from 2 to 8
move 1 from 2 to 8
move 26 from 9 to 3
move 18 from 3 to 8
move 1 from 2 to 1
move 12 from 3 to 8
move 1 from 2 to 3
move 3 from 6 to 4
move 1 from 1 to 9
move 11 from 8 to 5
move 1 from 4 to 7
move 9 from 3 to 9
move 1 from 7 to 8
move 11 from 8 to 3
move 11 from 3 to 2
move 11 from 2 to 9
move 19 from 9 to 8
move 3 from 5 to 7
move 2 from 4 to 2
move 2 from 2 to 8
move 29 from 8 to 2
move 5 from 5 to 4
move 1 from 9 to 6
move 2 from 5 to 9
move 1 from 6 to 9
move 7 from 8 to 7
move 1 from 9 to 7
move 6 from 9 to 1
move 1 from 9 to 4
move 1 from 5 to 4
move 15 from 2 to 5
move 3 from 1 to 7
move 5 from 5 to 2
move 1 from 8 to 3
move 1 from 5 to 8
move 2 from 3 to 6
move 1 from 3 to 8
move 9 from 2 to 1
move 1 from 8 to 7
move 1 from 8 to 3
move 10 from 7 to 8
move 4 from 7 to 3
move 1 from 7 to 2
move 1 from 8 to 6
move 3 from 6 to 5
move 6 from 5 to 8
move 3 from 1 to 3
move 8 from 3 to 7
move 3 from 1 to 3
move 4 from 8 to 3
move 1 from 4 to 5
move 4 from 1 to 4
move 1 from 4 to 5
move 1 from 7 to 4
move 4 from 4 to 1
move 2 from 8 to 7
move 6 from 5 to 2
move 2 from 8 to 1
move 6 from 4 to 7
move 1 from 5 to 4
move 5 from 8 to 6
move 1 from 6 to 9"""

class Instruction:
    def __init__(self, amount, f, to) -> None:
        self.amount = int(amount)
        self.f = int(f) - 1
        self.to = int(to) - 1
    
    def __repr__(self) -> str:
        return f'<amount: {self.amount}, from: {self.f}, to: {self.to}>'

def parse_input(input):
    stacks = []
    instructions = []
    lines = input.split('\n')
    for line in lines:
        if line.startswith(' 1'):
            start_state_index = lines.index(line)
            stack_amount = int(line.strip().split(' ')[-1])

            for i in range(0, stack_amount):
                stacks.append([])
        
        if line.startswith('move'):
            data = line.split(' ')
            instructions.append(Instruction(data[1], data[3], data[5]))

    top = lines[0:start_state_index]
    top.reverse()
    for line in top:
        # increments of 4
        start_index = 1
        for i in range(0, len(stacks)):
            element = line[start_index]
            if not element.isspace():
                stacks[i].append(element)
            start_index = start_index + 4

    return stacks, instructions


def puzzle_one_9000(input):
    stacks, instructions = parse_input(input)

    for instruction in instructions:
        for i in range(0, instruction.amount):
            stacks[instruction.to].append(stacks[instruction.f].pop())

    print("".join([l[-1] for l in stacks]))


def puzzle_two_9001(input):
    stacks, instructions = parse_input(input)

    for instruction in instructions:
        temp = []
        for i in range(0, instruction.amount):
            temp.append(stacks[instruction.f].pop())
        
        for element in range(0, len(temp)):
            stacks[instruction.to].append(temp.pop())

    print("".join([l[-1] for l in stacks]))


def main(input):
    puzzle_one_9000(input)
    puzzle_two_9001(input)


if __name__ == '__main__':
    main(example_start)
    main(actual)