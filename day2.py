

def is_invalid(id):
    id = str(id)
    mid = len(id) // 2
    return id[:mid] == id[mid:]

def better_is_invalid(id):
    id = str(id)
    for seq_end in range(1, len(id) // 2 + 1):
        sequence = id[:seq_end]
        all_the_same = True
        for i in range(seq_end, len(id), len(sequence)):
            if sequence != id[i:i + len(sequence)]:
                all_the_same = False

        if all_the_same:
            return True
    return False


def find_invalid(low, high):
    invalid = []
    for k in range(low, high + 1):
        if better_is_invalid(k):
            invalid.append(k)
    return invalid

with open('input2.txt') as file:
    contents = file.read()
    ranges = contents.split(",")
    total = 0
    for r in ranges:
        low, high = r.split("-")
        low = int(low)
        high = int(high)
        invalid = find_invalid(low, high)
        total += sum(invalid)


    print(f"Total of invalid ID's is {total}")

