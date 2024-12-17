from itertools import product
import sys

def parse_input(input_lines):
    equations = []
    for line in input_lines:
        line = line.strip()
        if not line or ":" not in line:
            continue
        target, numbers = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((target, numbers))
    return equations

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))

    print(f"Result for numbers:{numbers} {result}")
    return result

def is_solvable(target, numbers):
    # Generate all possible operator combinations
    operator_slots = len(numbers) - 1
    for operators in product(['+', '*', '||'], repeat=operator_slots):
        if evaluate_expression(numbers, operators) == target:
            return True
    return False

def calculate_total_calibration(input_data):
    input_lines = input_data.splitlines()
    equations = parse_input(input_lines)
    print(equations)
    total = 0
    for target, numbers in equations:
        if is_solvable(target, numbers):
            total += target
    return total

if __name__ == "__main__":
    input_data = sys.stdin.read()
    print(calculate_total_calibration(input_data))
