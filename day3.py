
def largest_joltage(bank):
    largest = 0
    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            if int(bank[i] + bank[j]) > largest:
                largest = int(bank[i] + bank[j])
    return largest

from pathlib import Path

def largest_after_removing(s: str, remove: int) -> str:
    stack = []
    for digit in s:
        while remove and stack and stack[-1] < digit:
            stack.pop()
            remove -= 1
        stack.append(digit)
    # remove remaining from the end if needed
    while remove:
        stack.pop()
        remove -= 1
    return ''.join(stack)

data = Path("input3.txt").read_text().strip().splitlines()
total = 0
for line in data:
    s = line.strip()
    best = largest_after_removing(s, len(s) - 12)
    total += int(best)

print(total)
