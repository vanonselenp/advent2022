example = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

empty = "......."

shapes = [
    [
        "..@@@@."
    ],
    [
        "...@...", 
        "..@@@..", 
        "...@..."
    ],
    [
        "....@..",
        "....@..",
        "..@@@.."
    ],
    [
        "..@....",
        "..@....",
        "..@....",
        "..@...."
    ],
    [
        "..@@...",
        "..@@..."
    ]
]


def visualize(grid):
    print()

    for y in grid:
        print('|', end='')
        print("".join(y), end='')
        print('|')
    print("+-------+")


def new_rock(grid, current_rock):


    return shapes[current_rock] + [empty, empty, empty] + grid, len(shapes[current_rock]) - 1


def move_down(grid, index):
    changed = False

    next = index + 1
    if grid[next] == empty:
        grid = [empty] + grid[0:next] + grid[next + 1:]


        changed = True

    return grid, changed


def main(input):
    grid = ["..####."]
    current_rock = 2

    grid, start_row = new_rock(grid, current_rock)

    visualize(grid)

    for i in range(start_row, len(grid) - 1):
        grid, changed = move_down(grid, i)

        if not changed:
            break

        visualize(grid)

if __name__ == '__main__':
    main(example)