from functools import lru_cache

def generate_reversed_adjacency(adjacency):
    rev_adj = {}
    for node in adjacency:
        rev_adj[node] = []
        for k, v in adjacency.items():
            if node in v:
                rev_adj[node].append(k)

    rev_adj['out'] = []
    for k, v in adjacency.items():
        if 'out' in v:
            rev_adj['out'].append(k)
    return rev_adj

adjacency = {}
with open('input11.txt') as file:
    for line in file:
        split_line = line.split(":")
        source = split_line[0]
        dest = split_line[1]
        dest = dest.strip().split(" ")

        adjacency[source] = dest


rev_adjacency = generate_reversed_adjacency(adjacency)

@lru_cache(None)
def count_paths(node):
    if node == 'you':
        return 1
    else:
        total = 0
        for adj in rev_adjacency[node]:
            total += count_paths(adj)
        return total

seen = dict()

def count_paths_svr(node, has_dac, has_fft):
    key = (node, has_dac, has_fft)
    if key in seen:
        return seen[key]

    if node == 'svr':
        return int(has_dac and has_fft)

    has_dac |= (node == 'dac')
    has_fft |= (node == 'fft')

    total = 0
    for adj in rev_adjacency.get(node, []):
        total += count_paths_svr(adj, has_dac, has_fft)

    seen[key] = total
    return total

num_paths = count_paths('out')
print(f'There are {num_paths} paths from "you" to "out"')


num_paths_svr = count_paths_svr('out', False, False)
print(f'There are {num_paths_svr} paths from "you" to "out" containing "dac" and "fft"')
