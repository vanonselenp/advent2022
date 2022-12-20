import json
import math

example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

actual = """Monkey 0:
  Starting items: 75, 75, 98, 97, 79, 97, 64
  Operation: new = old * 13
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 1:
  Starting items: 50, 99, 80, 84, 65, 95
  Operation: new = old + 2
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 5

Monkey 2:
  Starting items: 96, 74, 68, 96, 56, 71, 75, 53
  Operation: new = old + 1
  Test: divisible by 11
    If true: throw to monkey 7
    If false: throw to monkey 3

Monkey 3:
  Starting items: 83, 96, 86, 58, 92
  Operation: new = old + 8
  Test: divisible by 17
    If true: throw to monkey 6
    If false: throw to monkey 1

Monkey 4:
  Starting items: 99
  Operation: new = old * old
  Test: divisible by 5
    If true: throw to monkey 0
    If false: throw to monkey 5

Monkey 5:
  Starting items: 60, 54, 83
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 6:
  Starting items: 77, 67
  Operation: new = old * 17
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 1

Monkey 7:
  Starting items: 95, 65, 58, 76
  Operation: new = old + 5
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 6"""


def parse(input):
    monkies = input.split('\n\n')

    monks = {}

    for monkey in monkies:
        lines = monkey.split('\n')
        number = lines[0].split()[1][:-1]
        items = [int(x) for x in lines[1].split(':')[1].split(',')]
        divisible = lines[3].split()[3]
        true_pass = lines[4].split()[5]
        false_pass = lines[5].split()[5]
        command = lines[2].split('=')[1]

        monks[number] = {
            'items': items,
            'divisible': int(divisible),
            'true': true_pass,
            'false': false_pass,
            'command': command,
            'inspect': 0
        }

    return monks

def main(input):
    monkies = parse(input)

    hack = math.prod([x['divisible'] for x in monkies.values()])

    for round in range(0, 10000):
        for key, monkey in monkies.items():
            for item in monkey['items']:
                old = item
                worry = eval(monkey['command'])
                worry = worry % hack
                if worry % monkey['divisible'] == 0:
                    monkies[monkey['true']]['items'].append(worry)
                else:
                    monkies[monkey['false']]['items'].append(worry)
                
                monkey['inspect'] = monkey['inspect'] + 1
            monkey['items'] = []
    
    print(json.dumps(monkies, indent=2))

    things = [x['inspect'] for x in monkies.values()]
    things.sort()

    a, b = things[-2:]

    print(a * b)



if __name__ == '__main__':
    # main(example)
    main(actual)

# Monkey 0: 20, 23, 27, 26
# Monkey 1: 2080, 25, 167, 207, 401, 1046
# Monkey 2: 
# Monkey 3: 

# Monkey 0: 10, 12, 14, 26, 34
# Monkey 1: 245, 93, 53, 199, 115
# Monkey 2: 
# Monkey 3: 