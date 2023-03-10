import sys

example = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


actual = """Valve NA has flow rate=0; tunnels lead to valves MU, PH
Valve NW has flow rate=0; tunnels lead to valves KB, MH
Valve MR has flow rate=0; tunnels lead to valves GC, FI
Valve XD has flow rate=0; tunnels lead to valves UN, CN
Valve HK has flow rate=0; tunnels lead to valves AA, IF
Valve JL has flow rate=0; tunnels lead to valves IF, WB
Valve RQ has flow rate=13; tunnels lead to valves BL, DJ
Valve AB has flow rate=0; tunnels lead to valves BO, RU
Valve PE has flow rate=0; tunnels lead to valves AZ, IF
Valve QF has flow rate=0; tunnels lead to valves TD, AZ
Valve BA has flow rate=0; tunnels lead to valves RF, GU
Valve SY has flow rate=0; tunnels lead to valves MH, MU
Valve NT has flow rate=0; tunnels lead to valves DJ, UN
Valve GU has flow rate=21; tunnels lead to valves VJ, BA, YP
Valve AZ has flow rate=12; tunnels lead to valves QF, PI, AS, PE
Valve WQ has flow rate=23; tunnels lead to valves VJ, UM, CN
Valve DR has flow rate=0; tunnels lead to valves GA, CQ
Valve UM has flow rate=0; tunnels lead to valves IE, WQ
Valve XI has flow rate=0; tunnels lead to valves IE, IF
Valve SS has flow rate=0; tunnels lead to valves CQ, MH
Valve IE has flow rate=22; tunnels lead to valves YP, UM, XI, XA
Valve BT has flow rate=24; tunnels lead to valves KB, BL, GA
Valve GA has flow rate=0; tunnels lead to valves DR, BT
Valve AR has flow rate=0; tunnels lead to valves IF, FI
Valve DJ has flow rate=0; tunnels lead to valves RQ, NT
Valve PI has flow rate=0; tunnels lead to valves FI, AZ
Valve WB has flow rate=0; tunnels lead to valves TD, JL
Valve OQ has flow rate=0; tunnels lead to valves ME, TD
Valve RU has flow rate=19; tunnel leads to valve AB
Valve IF has flow rate=7; tunnels lead to valves AR, JL, HK, PE, XI
Valve BO has flow rate=0; tunnels lead to valves ME, AB
Valve CN has flow rate=0; tunnels lead to valves WQ, XD
Valve HH has flow rate=0; tunnels lead to valves AA, FS
Valve AS has flow rate=0; tunnels lead to valves AA, AZ
Valve FS has flow rate=0; tunnels lead to valves HH, MH
Valve PQ has flow rate=0; tunnels lead to valves TD, AA
Valve AA has flow rate=0; tunnels lead to valves HH, CO, AS, HK, PQ
Valve ME has flow rate=18; tunnels lead to valves OQ, BO, PH
Valve RF has flow rate=0; tunnels lead to valves UN, BA
Valve MH has flow rate=8; tunnels lead to valves FS, NW, SS, SY
Valve YP has flow rate=0; tunnels lead to valves IE, GU
Valve FI has flow rate=11; tunnels lead to valves PI, MR, AR, CO, DI
Valve UU has flow rate=0; tunnels lead to valves CQ, MU
Valve CO has flow rate=0; tunnels lead to valves AA, FI
Valve TD has flow rate=16; tunnels lead to valves QF, GC, OQ, WB, PQ
Valve MU has flow rate=15; tunnels lead to valves SY, UU, NA
Valve BL has flow rate=0; tunnels lead to valves BT, RQ
Valve PH has flow rate=0; tunnels lead to valves ME, NA
Valve XA has flow rate=0; tunnels lead to valves IE, DI
Valve GC has flow rate=0; tunnels lead to valves TD, MR
Valve KB has flow rate=0; tunnels lead to valves BT, NW
Valve DI has flow rate=0; tunnels lead to valves XA, FI
Valve CQ has flow rate=9; tunnels lead to valves UU, DR, SS
Valve VJ has flow rate=0; tunnels lead to valves WQ, GU
Valve UN has flow rate=20; tunnels lead to valves NT, XD, RF"""


class Node:
    def __init__(self, input) -> None:
        data = input.split(' ')
        links = {}
        [links.setdefault(x.replace(',', ''), 1) for x in data[9:]]

        name = data[1]
        self.name = name
        self.open = False
        self.neighbours = links
        self.flow = int(data[4].split('=')[1][:-1])

    def __repr__(self) -> str:
        return f'Node({self.name}, {self.neighbours}, {self.flow}, {self.open})'


def calc_shortest_path(graph, start):
    shortest_path = {}
    previous_nodes = {}

    unvisited_nodes = [x for x in graph.keys()]
    for n in unvisited_nodes:
        shortest_path[n] = sys.maxsize
    shortest_path[start] = 0

    while unvisited_nodes:
        current = unvisited_nodes[0]
        for node in unvisited_nodes:
            if shortest_path[node] < shortest_path[current]:
                current = node

        neighbours = graph[current].neighbours.keys()
        
        for neighbour in neighbours:
            possible_value = shortest_path[current] + graph[current].neighbours[neighbour]
            # compare current node height to neighbour height. only go current or up

            if shortest_path[neighbour] > possible_value:
                shortest_path[neighbour] = possible_value
                previous_nodes[neighbour] = current

        unvisited_nodes.remove(current)
    return shortest_path


def parse(input):
    graph = {}
    for line in input.split('\n'):
        node = Node(line)
        graph[node.name] = node

    for n in graph.keys():
        shortest = calc_shortest_path(graph, n)
        for m in [x for x in graph.keys() if x != n]:
            graph[n].neighbours[m] = shortest[m]

    return graph


def bfs(graph, current, visited=[], parent_score=0, current_time=0, max_time=30):
    if current_time >= max_time or len(visited) > len([x for x in graph.values() if x.flow > 0]):
        return parent_score, visited

    node = graph[current]

    current_score = parent_score + node.flow * (max_time - current_time)

    max_score = 0
    max_neighbours = []
    for neighbour in node.neighbours.keys():
        if neighbour not in visited and graph[neighbour].flow > 0:
            result = bfs(graph, neighbour, visited + [neighbour], current_score, current_time + node.neighbours[neighbour] + 1, max_time)
            if result[0] > max_score:
                max_score = result[0]
                max_neighbours = result[1]

    return max_score, max_neighbours


def main(input):
    graph = parse(input)

    x = bfs(graph, "AA", ['AA'])

    print('end', x)
    print()

    score, visited = bfs(graph, "AA", ['AA'], 0, 0, 26)

    elephant = bfs(graph, "AA", visited, score, 0, 26)

    print(score, visited)
    print(elephant)


if __name__ == '__main__':
    # main(example)
    main(actual)

# 2881. where am i going wrong? too low