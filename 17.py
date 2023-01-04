example = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

shapes = [
    [
        "..####."
    ],
    [
        "...#...", 
        "..###..", 
        "...#..."
    ],
    [
        "....#..",
        "....#..",
        "..###.."
    ],
    [
        "..#....",
        "..#....",
        "..#....",
        "..#...."
    ],
    [
        "..##...",
        "..##..."
    ]
]


def visualize(grid):
    for y in grid:
        print('|', end='')
        print("".join(y), end='')
        print('|')
    print("+-------+")


def new_rock(grid, current_rock):
    return shapes[current_rock] + [".......", ".......", "......."] + grid



def main(input):
    grid = []
    current_rock = 0

    grid = new_rock(grid, current_rock)
    visualize(grid)

    for i in range(0, len(grid) - 1):
        grid[i], grid[i + 1] = grid[i + 1], grid[i]
        visualize(grid)

if __name__ == '__main__':
    main(example)