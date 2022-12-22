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

    return output, {'min': {'x': min_x, 'y': min_y}, 'max': {'x': max_x, 'y': max_y}}


def build_grid(sensors, sizes):
    print(sizes)
    grid = []
    for x in range(sizes['min']['x'], sizes['max']['x'] + 1):
        row = []
        for y in range(sizes['min']['y'], sizes['max']['y'] + 1):
            row.append('.')
        grid.append(row)

    for group in sensors:
        sensor, beacon = group
        print(sensor, [sensor[0] - sizes['min']['x'], sensor[1] - sizes['min']['y']])
        grid[sensor[0] - sizes['min']['x']][sensor[1] - sizes['min']['y']] = 'S'
        grid[beacon[0] - sizes['min']['x']][beacon[1] - sizes['min']['y']] = 'B'

    return grid


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
    main(example)