import sys
import time
 
 
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



def parse_flow(data):
    parts = data.split('=')
    return int(parts[1].strip(';'))
 
 
def parse(data):
    lines = data.split('\n')
    valves = {}
 
    for line in lines:
        parts = line.split(' ')
        name = parts[1]
        flow = parse_flow(parts[4])
        kids = [kid.strip(',') for kid in parts[9:]]
 
        valves[name] = (flow, kids)
 
    return valves
 
 
def find_dists(valves, start):
    dists = {start: 0}
    seen = {start}
    dist = 0
    to_visit = valves[start][1]
 
    while len(to_visit) > 0:
        next_nodes = []
        dist += 1
 
        for item in to_visit:
            seen.add(item)
            dists[item] = dist
 
            kids = valves[item][1]
            for kid in kids:
                if not kid in seen:
                    next_nodes.append(kid)
 
        to_visit = next_nodes
 
    return dists
 
 
def build_dist_map(valves):
    dist_map = {}
 
    for name in valves:
        dist_map[name] = find_dists(valves, name)
 
    return dist_map
 
 
def walk_node(cfg, flows, node, max_time, cur_time, flow, seen):
    for target in cfg['to_open']:
        if target in seen:
            continue
 
        dists = cfg['dist_map'][node]
        to_target = dists[target]
        target_valve = cfg['valves'][target]
 
        new_time = cur_time + to_target + 1
        rem_time = max(0, max_time - new_time)
        new_flow = flow + (target_valve[0] * rem_time)
 
        if new_time < max_time:
            new_seen = set(seen)
            new_seen.add(target)
            new_seen = frozenset(new_seen)
 
            old_flow = flows[new_seen] if new_seen in flows else 0
            if new_flow > old_flow:
                flows[new_seen] = new_flow
 
            walk_node(cfg, flows, target, max_time,
                      new_time, new_flow, new_seen)
 
 
def walk(cfg, start, max_time):
    flows = {}
    walk_node(cfg, flows, start, max_time, 0, 0, frozenset())
    return flows
 
 
def part1(data):
    valves = parse(data)
    to_open = [name for name, (flow, _) in valves.items() if flow > 0]
    dist_map = build_dist_map(valves)
    cfg = {"valves": valves, "to_open": to_open, "dist_map": dist_map}
 
    flows = walk(cfg, "AA", 30)
    assert (max(flows.values()) == 1716)
 
 
def part2(data):
    valves = parse(data)
    to_open = [name for name, (flow, _) in valves.items() if flow > 0]
    dist_map = build_dist_map(valves)
    cfg = {"valves": valves, "to_open": to_open, "dist_map": dist_map}
 
    flows = walk(cfg, "AA", 26)
    items = list(flows.items())
 
    answer = 0
    for i in range(0, len(items)-1):
        s1, v1 = items[i]
 
        for j in range(i + 1, len(items)):
            s2, v2 = items[j]
 
            if s1.isdisjoint(s2) and v1 + v2 > answer:
                answer = v1 + v2
 
    print(answer)
 
    # data = f.read()
 
    # start = time.perf_counter()
    # part1(data)
    # print(f"Part1 {time.perf_counter() - start} secs")

start = time.perf_counter()
part2(actual)
print(f"Part2 {time.perf_counter() - start} secs")