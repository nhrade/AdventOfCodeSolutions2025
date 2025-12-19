
def find_spoiled_and_fresh(ingredients, ranges):
    fresh_ingredients = []
    spoiled_ingredients = []
    for ingredient in ingredients:
        is_fresh = False
        for r in ranges:
            if ingredient >= r[0] and ingredient <= r[1]:
                fresh_ingredients.append(ingredient)
                is_fresh = True
                break
        if not is_fresh:
            spoiled_ingredients.append(ingredient)
    return fresh_ingredients, spoiled_ingredients

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


with open('input5.txt') as file:
    contents = file.read().split("\n\n")
    ranges = [[int(line.split('-')[0]), int(line.split('-')[1])] for line in contents[0].splitlines()]
    ingredients = [int(i) for i in contents[1].splitlines()]
    fresh_ingredients, spoiled_ingredients = find_spoiled_and_fresh(ingredients, ranges)

    print(f"Fresh ingredients {fresh_ingredients}")
    print(f"Spoiled ingredients {spoiled_ingredients}")

    print(f"There are {len(fresh_ingredients)} fresh ingredients")

    merged_ranges = merge_intervals(ranges)

    num_fresh_ingredients = 0
    for r in merged_ranges:
        num_fresh_ingredients += abs(r[1] - r[0]) + 1

    print(f"There are {num_fresh_ingredients} total fresh ingredients")