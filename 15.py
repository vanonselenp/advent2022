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


def build_grid(sensors, sizes):
    print(sizes)
    grid = []
    for x in range(sizes['min']['x'], sizes['max']['x'] + 1):
        row = []
        for y in range(sizes['min']['y'], sizes['max']['y'] + 1):
            row.append('.')
        grid.append(row)

    index = 0
    for group in sensors:
        sensor, beacon = group
        grid[sensor[0] - sizes['min']['x']][sensor[1] - sizes['min']['y']] = 'S'
        grid[beacon[0] - sizes['min']['x']][beacon[1] - sizes['min']['y']] = 'B'
        distance = get_manhattan(sensor, beacon)

        print(distance)
        for x in range(sensor[0] - distance , sensor[0] + distance + 1):
            if not (x >= 0 and x < len(grid)):
                continue

            for y in range(sensor[1] - distance, sensor[1] + distance + 1):
                if not (y >= 0 and y < len(grid[0])):
                    continue

                if grid[x - sizes['min']['x']][y - sizes['min']['y']] == '.' and get_manhattan(sensor, [x, y]) <= distance:
                    grid[x - sizes['min']['x']][y - sizes['min']['y']]  = chr(index+97)

        index = index + 1

    return grid


def get_manhattan(sensor, becon):
    return abs(sensor[0] - becon[0]) + abs(sensor[1] - becon[1])


def visualise(grid):
    for y in range(0, len(grid[0])):
        for x in range(0, len(grid)):
            print(grid[x][y], end='')
        print()

def main(input):
    sensors, sizes = parse(input)

    grid = build_grid(sensors, sizes)

    visualise(grid)


if __name__ == '__main__':
    # main(example)
    main(example2)