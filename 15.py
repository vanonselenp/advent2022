import sys

example = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

example2 = """Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

actual = """Sensor at x=2832148, y=322979: closest beacon is at x=3015667, y=-141020
Sensor at x=1449180, y=3883502: closest beacon is at x=2656952, y=4188971
Sensor at x=2808169, y=1194666: closest beacon is at x=3015667, y=-141020
Sensor at x=1863363, y=2435968: closest beacon is at x=2166084, y=2883057
Sensor at x=3558230, y=2190936: closest beacon is at x=3244164, y=2592191
Sensor at x=711491, y=2444705: closest beacon is at x=617239, y=2988377
Sensor at x=2727148, y=2766272: closest beacon is at x=2166084, y=2883057
Sensor at x=2857938, y=3988086: closest beacon is at x=2968511, y=4098658
Sensor at x=1242410, y=2270153: closest beacon is at x=214592, y=2000000
Sensor at x=3171784, y=2523127: closest beacon is at x=3244164, y=2592191
Sensor at x=2293378, y=71434: closest beacon is at x=3015667, y=-141020
Sensor at x=399711, y=73420: closest beacon is at x=1152251, y=-158441
Sensor at x=3677529, y=415283: closest beacon is at x=3015667, y=-141020
Sensor at x=207809, y=2348497: closest beacon is at x=214592, y=2000000
Sensor at x=60607, y=3403420: closest beacon is at x=617239, y=2988377
Sensor at x=3767729, y=3136725: closest beacon is at x=4171278, y=3348370
Sensor at x=3899632, y=3998969: closest beacon is at x=4171278, y=3348370
Sensor at x=394783, y=1541278: closest beacon is at x=214592, y=2000000
Sensor at x=1193642, y=642631: closest beacon is at x=1152251, y=-158441
Sensor at x=122867, y=2661904: closest beacon is at x=214592, y=2000000
Sensor at x=551012, y=3787568: closest beacon is at x=617239, y=2988377
Sensor at x=3175715, y=2975144: closest beacon is at x=3244164, y=2592191
Sensor at x=402217, y=2812449: closest beacon is at x=617239, y=2988377
Sensor at x=879648, y=1177329: closest beacon is at x=214592, y=2000000
Sensor at x=1317218, y=2978309: closest beacon is at x=617239, y=2988377
Sensor at x=3965126, y=1743931: closest beacon is at x=3244164, y=2592191
Sensor at x=2304348, y=3140055: closest beacon is at x=2166084, y=2883057
Sensor at x=3380135, y=3650709: closest beacon is at x=2968511, y=4098658
Sensor at x=49224, y=1914296: closest beacon is at x=214592, y=2000000
Sensor at x=3096228, y=2457233: closest beacon is at x=3244164, y=2592191
Sensor at x=1415660, y=6715: closest beacon is at x=1152251, y=-158441
Sensor at x=2616280, y=3548378: closest beacon is at x=2656952, y=4188971"""

def parse(input):
    output = []

    nodes = []

    lines = input.split('\n')
    for line in lines:
        data = line.split(' ')

        sensor = [int(data[2].split('=')[1][:-1]), int(data[3].split('=')[1][:-1])]
        beacon = [int(data[8].split('=')[1][:-1]), int(data[9].split('=')[1])]

        output.append([sensor, beacon])
        nodes.append(beacon)
        nodes.append(sensor)

    min_x = sys.maxsize
    min_y = sys.maxsize
    max_x = 0
    max_y = 0

    for n in nodes:
        if n[0] < min_x:
            min_x = n[0]
        if n[1] < min_y:
            min_y = n[1]

        if n[0] > max_x:
            max_x = n[0]
        if n[1] > max_y:
            max_y = n[1]

    return output, {'min': {'x': min_x - 10, 'y': min_y - 10}, 'max': {'x': max_x + 10, 'y': max_y + 10}}

def fmt_key(x, y):
    return f'{x}:{y}'

def build_grid(sensors):
    grid = {}
    index = 0

    for group in sensors:
        sensor, beacon = group
        grid[fmt_key(sensor[0], sensor[1])] = 'S'
        grid[fmt_key(beacon[0], beacon[1])] = 'B'
        
        index = index + 1

    return grid


def get_manhattan(sensor, becon):
    return abs(sensor[0] - becon[0]) + abs(sensor[1] - becon[1])


def visualise(grid, sizes):
    for y in range(sizes['min']['y'], sizes['max']['y']):
        for x in range(sizes['min']['x'], sizes['max']['x']):
            print(grid.get(fmt_key(x, y), '.'), end='')
        print()

def get_entries_on_row(grid, sizes, sensors, y):
    total = 0

    min_dist = sys.maxsize
    max_dist = 0
    for sensor, becon in sensors:
        dist = get_manhattan(sensor, becon)
        if dist > max_dist:
            max_dist = dist

        if dist < min_dist:
            min_dist = dist

    for x in range(sizes['min']['x'] - max_dist, sizes['max']['x'] + max_dist):
        node = [x, y]
        for sensor, beacon in sensors:
            sensor_distance = get_manhattan(sensor, beacon)
            node_distance = get_manhattan(sensor, node)
            if sensor_distance >= node_distance:
                key = fmt_key(x, y)
                if key not in grid:
                    grid[key] = '#'
                    total = total + 1
    return total


def get_beacon(grid, sensors, range_max):
    total = 0
    found_y = None
    found_x = None

    for y in range(0, range_max):
        print(y)
        row = {}
        total = 0
        for x in range(0, range_max):

            node = [x, y]
            for sensor, beacon in sensors:
                sensor_distance = get_manhattan(sensor, beacon)
                node_distance = get_manhattan(sensor, node)
                if sensor_distance >= node_distance:
                    key = fmt_key(x, y)
                    if key not in grid and key not in row:
                        row[key] = '#'
                        total = total + 1
                    
                    elif key in grid and (grid[key] == 'S' or grid[key] == 'B'):
                        total = total + 1
        if range_max - total == 1:
            found_y = y
            break

    total = 0
    for x in range(0, range_max):
        node = [x, y]

        found = False

        for sensor, beacon in sensors:
            sensor_distance = get_manhattan(sensor, beacon)
            node_distance = get_manhattan(sensor, node)

            if sensor_distance >= node_distance:
                found = True
                break

        if found == False:
            return [x, found_y]

    return [found_x, found_y]


# def get_beacon_2(sensors):



def main(input, range_max):
    sensors, sizes = parse(input)

    grid = build_grid(sensors)

    # entries = get_entries_on_row(grid, sizes, sensors, 2000000)

    coords = get_beacon(grid, sensors, range_max)
   
    # visualise(grid, sizes)

    print(coords)


if __name__ == '__main__':
    main(example, 20)
    main(actual, 4000000)
    # main(example2)