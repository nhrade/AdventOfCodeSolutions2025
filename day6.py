

def find_grand_total(equations, operators):
    grand_total = 0
    for i, equation in enumerate(equations):
        operator = operators[i]
        total = equation[0]
        for k in equation[1:]:
            if operator == '*':
                total *= k
            elif operator == '+':
                total += k
        grand_total += total
    return grand_total


with open('input6.txt') as file:
    lines = file.read().splitlines()
    numbers = []
    for line in lines[:-1]:
        split_line = line.split()
        numbers.append([int(n) for n in split_line])
    operators = lines[-1].split()
    print(numbers)
    print(operators)
    equations = []
    for col, operator in enumerate(operators):
        col_numbers = []
        for row in range(len(numbers)):
            col_numbers.append(numbers[row][col])
        equations.append(col_numbers)

    grand_total = find_grand_total(equations, operators)
    print(f"Grand total is {grand_total}")