

tiles = []
with open('input9.txt') as file:
    for line in file:
        split_line = line.split(',')
        a = int(split_line[0])
        b = int(split_line[1])
        tiles.append((a, b))


def find_largest_rectangle(tiles):
    largest_area = 0
    for x0, y0 in tiles:
        for x1, y1 in tiles:
            if x0 != x1 and y0 != y1:
                area = (y1 - y0 + 1) * (x1 - x0 + 1)
                if area > largest_area:
                    largest_area = area
    return largest_area


largest_area = find_largest_rectangle(tiles)
print(f"The largest rectangle is {largest_area}")