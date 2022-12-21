import json
import copy
import sys

example = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

actual = """abcccccccccccccccccccccccccccccccccccccaaaaaaacccccccaaaaaaaaaaaccccccccccccccccccccaaacaaaaaaaacccccccccccccccccccccccccccccccccccaaaaa
abccccccccccccccccccaaccaacccccccccccccaaaaaaaccccccccaaaaaaaaaaacccccccaaaaccccccccaaaaaaaaaaaaacccccccccccccccccccccccccccccccccaaaaaa
abccccccccccccccccccaaaaaaccccccccccaaaccaaaaaacccccccaaaaaaaaaaccccccccaaaaccccccaaaaaaaaaaaaaaacccccccccccccccccccaaacccccccccccaaaaaa
abcccccccccccccccccccaaaaacccccccccccaaccaacaaaccccccaaaaaaaaaaaccccccccaaaacccccaaaaaaaaacaaaaaaacccccccccccccccccaaaacccccccccccaaacaa
abccccccccccccccccccaaaaaaccccccccaacaaaaaacccccccccaaaaaaaaaaaaacaaaccccaaccccccaaaaaaaaacaacccccccccccccccccaaaccaaaacccccccccccccccaa
abcccccccccccccccccaaaaaaaacccccccaaaaaaaaccccccaaaaaaaacaaaacaaaaaaacccccccccaaccccaaaaaacaaacccccccccccccccaaaakkkaaccccccccccccccccaa
abcccccccccccccccccaaaaaaaaccccccccaaaaaccccaacccaaaaaaaaaaaacaaaaaaccccccccccaacccaaaaaaaaaaaacccccccccccccccakkkkkklcccccccccccccccccc
abaaacccccccccccaaccccaaccccccccccccaaaaaccaaacccaaaaaaaaaaaaaaaaaaaaccccccaaaaaaaacaacccaaaaaaccccccccccccccckkkkkkkllcccccccaaaccccccc
abaaaacccccccaacaaccccaacccccccccccaaacaaaaaaaccccaaaaaaaaaaaaaaaaaaaacccccaaaaaaaaaaaccccaaaaacccccccccccccckkkksssllllccccccaaaaaacccc
abaaaacccccccaaaaacccccccccccaaaccccaacaaaaaaccccaaaaaacaaaaaaaaaaaaaacccccccaaaaccccccccaaaaacccccccccccccckkkksssssllllcccccaaaaaacccc
abaaacccccccccaaaaaaccccccccaaaaccccccccaaaaaaaacaaaaaaaaaaaaacaaacaaacccccccaaaaacccccccaaaaacccccccccccccjkkkrssssssllllccccccaaaccccc
abccccccccccaaaaaaaaccccccccaaaacccccccaaaaaaaaacaacaaaaaaaaaacaaaccccccccccaaacaaccccccccccccccccccccccccjjkkrrsuuussslllllcccccaaccccc
abccaaacccccaaaaacccccccccccaaaaccccccaaaaaaaaaacccccaaaaaaaaaacaaccccccccccaacccacccccccccccccccccccccjjjjjjrrrsuuuussslllllmcccddacccc
abcccaaaccaccacaaaccccccccccccccccccccaaaaaaaccccccccccaaaaaaaaccccccaacccccccccccaaaaacccccccccccccccjjjjjjrrrruuuuuusssllmmmmmddddcccc
abccaaaaaaaacccaaaccccccccccccccccaaacccccaaaccccccccccccaaacccccccccaacccccccccccaaaaacccccccccccccjjjjjrrrrrruuuxuuussqqqqmmmmmdddcccc
abcaaaaaaaacccaaaaaacaaaaaccccccaaaaaaccccaaacccaaccccccccaaccccccaaaaaaaaccaaacccaaaaaaccccccccccccjjjjrrrrrruuuxxxuuuqqqqqqqmmmdddcccc
abaaaaaaaaaccccaaaaacaaaaaccccccaaaaaaaaccccccaaaaaaccccccccccccccaaaaaaaaccaaacaaaaaaaacccccccccccjjjjrrrtttuuuuxxxyvvvvvqqqqmmmdddcccc
abaaaaaaaaaccaaaaaaacaaaaaaccccccaaaaaaaacccccaaaaaaccccccccccccccccaaaaccaaaaaaaaaaaaaacccccccccaaiijqqqrttttuuuxxyyvvvvvvvqqmmmdddcccc
abcaaaaaaaaccaaaaaaaaaaaaaacccccaaaaaaaacccccccaaaacccccaaaaccccccccaaaaacaaaaaaaaccaaccccccccccaaaiiiqqqttttxxxxxxyyyyyyvvvqqmmmdddcccc
abcccaaaaaaacaaaaaaaaaaaaaacccccaaaaaaaaaaaccccaaaaccccaaaaacccccccaaaaaacaaaaaaacccccccccccccccaaaiiiqqqtttxxxxxxxyyyyyyvvqqqmmmdddcccc
SbcccaacccaccccaaacacccaaacccccccccaaaaaaaaacccaccaccccaaaaaaccccccaaccaacccaaaaaccccccccccccccccaaiiiiqqtttxxxxEzzzyyyyvvvqqqmmmddccccc
abccaaaccccccccaaccccccccccccccccccaaaaaaaaccccccccccccaaaaaaccccccccccccccaaacaaaccaacccccccccccccciiiqqqttttxxxyyyyyvvvvqqqmmmdddccccc
abccccccccccccccccccccccccccccccccaaaaaaaccccccccccccccaaaaaacccccccccccccccaacccccaaaaaaaccccccccccciiiqqqttttxxyyyyyvvvrrrnnneeecccccc
abcaaaaccccccccccccccccccccccccccaaaaaaaaccccccccccccccccaacccccccccccccccccccccccccaaaaacccccccccccciiiqqqqttxxyyyyyyyvvrrnnnneeecccccc
abcaaaaacccccccccccccccccccccccccaaaacaaacccaccaaacccccccccccccccccccccccccaaaccccaaaaaaaccccccccccccciiiqqqttwwyywwyyywwrrnnneeeccccccc
abaaaaaacccaccaccccccccccccccccccaaaaccaacccaaaaaaccccccccccccccccaaaccccaaaaaacccaaaaaaaacccccccccccciiiqqqtswwwwwwwwwwwrrnnneeeccccccc
abaaaaaacccaaaaccccccccaaaacccccccaaacccccccaaaaaacccccccccccccccaaaaaaccaaaaaacccaaaaaaaacaaccccccaaciiiqppsswwwwsswwwwwrrrnneeeccccccc
abcaaaaacccaaaaacccccccaaaacccccccccccccccccaaaaaaaccccccccccccccaaaaaaccaaaaaacccccaaaaaaaaaccccccaaaahhpppssswwsssswwwwrrrnneeeacccccc
abcaaaccccaaaaaacccccccaaaaccccccccccccccccaaaaaaaaccccccccccccccaaaaacccaaaaaccccccaacaaaaaaaaccaaaaaahhpppsssssssssrrrrrrnnneeeacccccc
abccccccccaaaaaaccccccccaacccccccccccccccccaaaaaaaaccccaacccccccccaaaaaccaaaaacccccccccaaaaaaaaccaaaaachhpppssssssoosrrrrrrnnneeeaaacccc
abccccccccccaaccccccccccccccccaaaaaccccccaacccaaacccaaaaacccccccccaacaacccccccccccccccccaaaaaaacccaaaaahhhppppssppooooorroonnffeaaaacccc
abaaccccccccccccccccccccccccccaaaaaccccccaacccaaaccccaaaaacccccccccccccccccccccccccccaacaaaaacccccaacaahhhppppppppoooooooooonfffaaaacccc
abaccccccccccccccccccccccccccaaaaaacccaaaaaaaacccccccaaaaaccccccccccccccccccccccccaaaaaaaaaaaccccccccccchhhpppppppgggoooooooffffaacccccc
abaccccccccccccccccccccccccccaaaaaacccaaaaaaaaccccccaaaaaccccccacccaacccccccccccccaaaaaccccaaccccccccccchhhhhhggggggggfffffffffaaacccccc
abaacccccccccccccccccccccccccaaaaaacccccaaaacccccccccaaaacccaacaacaaacccccccccccccaaaaaaacccccccccccccccchhhhgggggggggffffffffccaacccccc
abcccccccaacccccccccccccccccccaaaccccccaaaaaccccccccaaaaccaaaacaaaaacccccccccccccaaaaaaaaccccccccccccccccchhhggggaaaagffffffcccccccccccc
abcccccccaacccccccccccccaacccccccccccccaaaaaaccaaccccaaaaaaaaacaaaaaacccccccaaaacaaaaaaaacccccccccccaacccccccaaaacaaaacccccccccccccccccc
abccccaaaaaaaacccccccaacaaaccccccccccccaaccaacaaaacccaaaaaaaacaaaaaaaaccccccaaaaccacaaaccaaaccccaaaaaacccccccaacccaaaacccccccccccccaaaaa
abccccaaaaaaaacccccccaaaaaccccccccccccccccccccaaaaccccaaaaaaacaaaaaaaaccccccaaaaccccaaaccaaaaaccaaaaaaaacccccccccccaaaccccccccccccccaaaa
abccccccaaaaccccccccccaaaaaaccccccccccccccccccaaaacccaaaaaaaaaaccaaccccccccccaacccccccccaaaaacccaaaaaaaacccccccccccaaaccccccccccccccaaaa
abcccccaaaaaacccccccaaaaaaaacccccccccccccccccccccccaaaaaaaaaaaaaaaacccccccccccccccccccccaaaaaacccaaaaaaaccccccccccccccccccccccccccaaaaaa"""

def get_x_y(input, world,looking):
    cleaned = input.replace('\n', '')
    return "%s:%s" % (int(cleaned.index(looking) / len(world[0])), cleaned.index(looking) % len(world[0]))

def parse(input):
    world = [[ord(c) - 96 if c.islower() else 1 if c == 'S' else 26 for c in line] for line in input.split('\n')]
    start = get_x_y(input, world, 'S')
    end = get_x_y(input, world, 'E')

    return world, start, end

def visualise(world, previous):
    for x in range(0, len(world)):
        for y in range(0, len(world[x])):
            print(chr(world[x][y] + 96) if f'{x}:{y}' in previous else ' ', end='')
        print()

def find_accessible_neighbours(world, key):
    possible = []

    current = {'x': int(key.split(':')[0]), 'y': int(key.split(':')[1])}
    locations = [
        {'x': -1, 'y': 0},
        {'x': 1, 'y': 0},
        {'x': 0, 'y': 1},
        {'x': 0, 'y': -1},
    ]

    for l in locations:
        check = {'x': current['x'] + l['x'], 'y': current['y'] + l['y']}

        inbounds =  check['x'] >= 0 and check['x'] < len(world) and check['y'] >= 0 and check['y'] < len(world[check['x']]) 
        if not inbounds:
            continue

        # can_move = abs(world[current['x']][current['y']] - world[check['x']][check['y']]) < 2
        can_move = world[current['x']][current['y']] > world[check['x']][check['y']] or abs(world[current['x']][current['y']] - world[check['x']][check['y']]) < 2
        if can_move:
            possible.append(check)

    return ["%s:%s" % (node['x'], node['y']) for node in possible]

def generate_nodes(world):
    result = []
    [[result.append("%s:%s" % (x, y)) for y in range(0, len(world[x]))] for x in range(0, len(world))]
    return result

def part_one(world, start, end):
    nodes = generate_nodes(world)

    shortest_path = {}
    previous_nodes = {}

    for n in nodes:
        shortest_path[n] = sys.maxsize
    shortest_path[start] = 0

    unvisited_nodes = generate_nodes(world)

    # while end not in previous_nodes:
    while unvisited_nodes:
        current = unvisited_nodes[0]
        for node in unvisited_nodes:
            if shortest_path[node] < shortest_path[current]:
                current = node

        neighbours = find_accessible_neighbours(world, current)
        
        if (shortest_path[current] == 9223372036854775807):
            break

        for neighbour in neighbours:
            possible_value = shortest_path[current] + 1
            # compare current node height to neighbour height. only go current or up

            if shortest_path[neighbour] > possible_value:
                shortest_path[neighbour] = possible_value
                previous_nodes[neighbour] = current

        unvisited_nodes.remove(current)

    return shortest_path, previous_nodes


def main(input):
    world, start, end = parse(input)

    shortest_path, previous_nodes = part_one(world, start, end)

    # print(previous_nodes, shortest_path)
    print(shortest_path[end], end)
    # print(previous_nodes)
    # visualise(world, previous_nodes)

if __name__ == '__main__':
    main(example)
    main(actual)

#  01234567
#0 v..v<<<<
#1 >v.vv<<^
#2 .>vv>E^^
#3 ..v>>>^^
#4 ..>>>>>^