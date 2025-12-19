import copy
grid = []

with open('input4.txt') as file:
    for line in file:
        cells = []
        for c in line.strip():
            cells.append(c)
        grid.append(cells)


num_rows = len(grid)
num_cols = len(grid[0])


def print_grid(grid):
    for r in range(num_rows):
        for c in range(num_cols):
            print(grid[r][c], end='')
        print()

def get_adjacent(grid, position):
    r, c = position
    adjacent = []
    if r > 0:
        adjacent.append((r - 1, c))
    if c > 0:
        adjacent.append((r, c - 1))
    if r > 0 and c > 0:
        adjacent.append((r - 1, c - 1))

    if r < num_rows - 1:
        adjacent.append((r + 1, c))

    if c < num_cols - 1:
        adjacent.append((r, c + 1))

    if r < num_rows - 1 and c < num_cols - 1:
        adjacent.append((r + 1, c + 1))

    if r > 0 and c < num_cols - 1:
        adjacent.append((r - 1, c + 1))

    if r < num_rows - 1 and c > 0:
        adjacent.append((r + 1, c - 1))

    return adjacent


def count_adjacent_rolls(grid, r, c):
    adjacent = get_adjacent(grid, (r, c))
    count = 0
    for cell in adjacent:
        if grid[cell[0]][cell[1]] == '@':
            count += 1
    return count

def is_accessible(grid, r, c):
    return count_adjacent_rolls(grid, r, c) < 4

def count_accessible_rolls(grid):
    total = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == '@' and is_accessible(grid, r, c):
                total += 1
    return total


def any_accessible(grid):
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == '@' and is_accessible(grid, r, c):
                return True
    return False


def remove_accessible(grid):
    grid_copy = copy.deepcopy(grid)
    num_removed = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if grid_copy[r][c] == '@' and is_accessible(grid, r, c):
                grid_copy[r][c] = '.'
                num_removed += 1
    return grid_copy, num_removed

def remove_all_accessible(grid):
    total_removed = 0
    i = 0
    while any_accessible(grid):
        grid, num_removed = remove_accessible(grid)
        print(f"Num removed at {i} = {num_removed}")
        total_removed += num_removed
        i += 1
    return grid, total_removed


print_grid(grid)
print(f"initial accessible rolls {count_accessible_rolls(grid)}")

grid, total_removed = remove_all_accessible(grid)
print(f"Number of removed rolls {total_removed}")
