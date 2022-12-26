import json
import sys
import copy
import functools

#aa, dd, bb, jj, hh, ee, cc, 
#['AA', 'DD', 'JJ', 'BB', 'HH', 'EE', 'CC']
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

unique = set()

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

        neighbours = graph[current]['links'].keys()
        
        for neighbour in neighbours:
            possible_value = shortest_path[current] + graph[current]['links'][neighbour]
            # compare current node height to neighbour height. only go current or up

            if shortest_path[neighbour] > possible_value:
                shortest_path[neighbour] = possible_value
                previous_nodes[neighbour] = current

        unvisited_nodes.remove(current)
    return shortest_path


def parse(input, start):
    lines = input.split('\n')
    graph = {}
    for line in lines:
        data = line.split(' ')
        links = {}
        [links.setdefault(x.replace(',', ''), 1) for x in data[9:]]
        graph[data[1]] = {
            'name': data[1], 
            'flow': int(data[4].split('=')[1][:-1]), 
            'links': links, 
            'open': False
        }


    # collapse the grid
    zeros = [x for x in graph.values() if x['flow'] == 0 and x['name'] != start]

    # left - z - right
    for z in zeros:

        for left in z['links'].keys():
            rights = [x for x in z['links'].keys() if x != left]

            if z['name'] in graph[left]['links']:
                left_cost = graph[left]['links'][z['name']]

                for right in rights:
                    cost = left_cost + graph[right]['links'][z['name']]
                    graph[left]['links'][right] = cost
                    graph[right]['links'][left] = cost

        for left in z['links'].keys():
            graph[left]['links'].pop(z['name'])

        graph.pop(z['name'])

    for n in graph.keys():
        shortest = calc_shortest_path(graph, n)
        for m in [x for x in graph.keys() if x != n]:
            graph[n]['links'][m] = shortest[m]
                
    print(json.dumps(graph, indent=2))
    return graph


def current_flow(graph):
    return sum([v['flow'] for v in graph.values() if v['open']])


def dfs(visited, graph, node):
    # print('dfs', visited, node)
    if node not in visited:
        visited.append(node)

        short_hops_first = sorted([x for x in graph[node]['links'].items()], key=lambda n: n[1])
        neighbours = short_hops_first

        for neighbour in neighbours:
            dfs(visited, graph, neighbour[0])

random_stuff = {}

def cost_cutter(graph, node, visited):
    if len(visited) == len(graph.keys()):
        return visited

    current = graph[node]

    max_value = 0
    max_neighbour = list(current['links'].keys())[0]

    for neighbour in  current['links'].keys():

        for link in graph[neighbour]['links'].keys():
            for second in graph[link]['links'].keys():
                for third in graph[second]['links'].keys():
                    if neighbour not in visited:
                        neighbour_visited = list(dict.fromkeys(visited + [neighbour, link, second, third]))
                        dfs(neighbour_visited, graph, neighbour), copy.deepcopy(graph)
                        current_value = calculate_cost(neighbour_visited, copy.deepcopy(graph))
                        random_stuff[','.join(neighbour_visited)] = current_value
                        if current_value > max_value:
                            print("updated", max_value, current_value, neighbour, visited, neighbour_visited)
                            max_value = current_value
                            max_neighbour = neighbour
    
    print("mox value", max_value)

    return cost_cutter(graph, max_neighbour, visited + [max_neighbour])


def calculate_cost(visited, graph):
    current = visited[0]
    left = visited[1:]

    total = 0

    cost = 1
    delay = 0
    while cost < 31:
        opened = [x['name'] for x in graph.values() if x['open']]
        pressure = sum([graph[x]['flow'] for x in opened])
        total = total + pressure
        if delay > 0:
            delay = delay - 1
        elif graph[current]['open'] == False and graph[current]['flow'] > 0:
            graph[current]['open'] = True
            cost = cost + 1
        elif len(left) > 0:
            cost = cost + graph[current]['links'][left[0]]
            delay = graph[current]['links'][left[0]] - 1
            current = left[0]
            left = left[1:]
        else:
            cost = cost + 1

    return total


def calculate_cost_with_output(visited, graph):
    print(visited)
    current = visited[0]
    left = visited[1:]

    total = 0

    cost = 1
    delay = 0
    while cost < 31:
        print(f'=== Minute {cost - delay} ===')
        opened = [x['name'] for x in graph.values() if x['open']]
        pressure = sum([graph[x]['flow'] for x in opened])
        total = total + pressure
        print(f'Valves open: {opened}')
        print(f'Currently in {current}')
        print(f'PRESSURE in {pressure}')
        if delay > 0:
            delay = delay - 1
        elif graph[current]['open'] == False and graph[current]['flow'] > 0:
            graph[current]['open'] = True
            cost = cost + 1
        elif len(left) > 0:
            # print( graph[current], left[0])
            cost = cost + graph[current]['links'][left[0]]
            delay = graph[current]['links'][left[0]] - 1
            # cost = cost + sum([v for k, v in graph[current]['links'].items() if k == left[0]])
            current = left[0]
            left = left[1:]
        else:
            cost = cost + 1

        print()

    print(f'Total Pressure: {total}')

    return total


def main(input, start):
    graph = parse(input, start)

    # output = brute_fcost_cutterorce(graph, start, [start])

    print(calculate_cost_with_output(cost_cutter(copy.deepcopy(graph), start, [start]), graph))
    costs = list(random_stuff.values())
    costs.sort(reverse=True)
    print(costs[0])
    # print(json.dumps(list(unique), indent=2), len(list(unique)))

    # calculate_cost(visited, copy.deepcopy(graph))

    # visited = []

    # dfs(visited, graph, start)
    # calculate_cost(visited, copy.deepcopy(graph))
    # output = th?ing(graph, start, [start])

    # print(unique, len(unique))

    # print([graph[x]['flow'] for x in visited])
    # print([graph[x]['name'] for x in visited])

    # totals = []
    # for i in list(unique):
    #     totals.append(calculate_cost(i.split(','), copy.deepcopy(graph)))

    # totals.sort(reverse=True)
    # print(totals[0])


if __name__ == "__main__":
    # main(example, 'AA')
    main(actual, 'NA')