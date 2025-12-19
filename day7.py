from collections import deque

def find_start(manifold):
    for r in range(len(manifold)):
        for c in range(len(manifold[0])):
            if manifold[r][c] == 'S':
                return r, c
    return -1, -1


def print_manifold(manifold):
    for r in range(len(manifold)):
        for c in range(len(manifold[0])):
            print(manifold[r][c], end='')
        print()

    print('\n')

from collections import deque

def find_start(manifold):
    for r, row in enumerate(manifold):
        for c, val in enumerate(row):
            if val == 'S':
                return r, c
    return None, None


def count_splits_fast(manifold):
    R, C = len(manifold), len(manifold[0])
    sr, sc = find_start(manifold)

    # Start beam is one below S
    queue = deque([(sr + 1, sc)])
    visited = set()
    split_count = 0

    while queue:
        r, c = queue.popleft()

        # Out of bounds?
        if not (0 <= r < R and 0 <= c < C):
            continue

        # If we've been here before, skip
        if (r, c) in visited:
            continue
        visited.add((r, c))

        cell = manifold[r][c]

        if cell == '^':
            # Split
            split_count += 1

            # Emit left and right
            queue.append((r + 1, c - 1))
            queue.append((r + 1, c + 1))

        else:
            # Beam continues downward
            queue.append((r + 1, c))

    return split_count


def count_all_timelines(manifold):
    start = find_start(manifold)
    return count_timelines(manifold, start) + 1

seen_positions = {}
def count_timelines(manifold, position):
    r, c = position
    if r >= len(manifold):
        return 0
    else:
        if manifold[r][c] == '^':
            if (r, c) in seen_positions:
                return seen_positions[(r, c)]
            else:
                left_count = count_timelines(manifold, (r, c - 1))
                right_count = count_timelines(manifold, (r, c + 1))
                total = 1 + left_count + right_count
                seen_positions[(r, c)] = total
                return total
        else:
            return count_timelines(manifold, (r + 1, c))



with open('input7_test.txt') as file:

    manifold = []
    data = file.read().splitlines()
    for line in data:
        manifold.append([])
        for c in line:
            manifold[-1].append(c)

    total_splits = count_splits_fast(manifold)
    print(f"There are {total_splits} splits of the tachyon beam.")

    num_timelines = count_all_timelines(manifold)
    print(f"There are {num_timelines} timelines of the tachyon beam.")