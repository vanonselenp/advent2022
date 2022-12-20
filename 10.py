example = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


example2 = """noop
addx 3
addx -5"""

actual = """noop
addx 10
addx -4
addx -1
noop
noop
addx 5
addx -12
addx 17
noop
addx 1
addx 2
noop
addx 3
addx 2
noop
noop
addx 7
addx 3
noop
addx 2
noop
noop
addx 1
addx -38
addx 5
addx 2
addx 3
addx -2
addx 2
addx 5
addx 2
addx -4
addx 26
addx -19
addx 2
addx 5
addx -2
addx 7
addx -2
addx 5
addx 2
addx 4
addx -17
addx -23
addx 1
addx 5
addx 3
noop
addx 2
addx 24
addx 4
addx -23
noop
addx 5
addx -1
addx 6
noop
addx -2
noop
noop
noop
addx 7
addx 1
addx 4
noop
noop
noop
noop
addx -37
addx 5
addx 2
addx 1
noop
addx 4
addx -2
addx -4
addx 9
addx 7
noop
noop
addx 2
addx 3
addx -2
noop
addx -12
addx 17
noop
addx 3
addx 2
addx -3
addx -30
addx 3
noop
addx 2
addx 3
addx -2
addx 2
addx 5
addx 2
addx 11
addx -6
noop
addx 2
addx -19
addx 20
addx -7
addx 14
addx 8
addx -7
addx 2
addx -26
addx -7
noop
noop
addx 5
addx -2
addx 5
addx 15
addx -13
addx 5
noop
noop
addx 1
addx 4
addx 3
addx -2
addx 4
addx 1
noop
addx 2
noop
addx 3
addx 2
noop
noop
noop
noop
noop"""

totals = []
screen = []

def process_commands(commands, state, cycles):
    if len(commands) == 0:
        return state

    command = commands[0]

    if (cycles - 20) % 40 == 0:
        totals.append(state['X'] * cycles)

    current = cycles % 40
    value = state['X'] - 1 if command[0] == 'delay' else state['X']
    value = state['X'] if command[0] == 'delay' else state['X'] - 1
    value = state['X']
    if value in range(current - 2, current + 1):
        screen.append('#')
    else:
        screen.append('.')

    if command[0] == 'noop':
        return process_commands(commands[1:], state, cycles + 1)

    if command[0] == 'addx':
        return process_commands([['delay', command[1]]] + commands[1:], state, cycles + 1)

    if command[0] == 'delay':
        state['X'] = state['X'] + int(command[1])
        return process_commands(commands[1:], state, cycles + 1)


def main(input):
    commands = [x.split() for x in input.split('\n')]

    state = process_commands(commands, {'X': 1}, 1)

    print(state)

    print(sum(totals))


    for i in range(0, len(screen)):
        if i % 40 == 0:
            print()
        print(screen[i], end='')



if __name__ == '__main__':
    # main(example2)
    # main(example)
    main(actual)