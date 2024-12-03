import re
import sys

def multiply(string):
    # Patterns to match
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")

    # Find all instructions and save them with positions and also add x,y groups for mul instruction
    instructions = []
    for m in mul_pattern.finditer(string):
        instructions.append(('mul', m.start(), m.groups()))
    for m in do_pattern.finditer(string):
        instructions.append(('do', m.start()))
    for m in dont_pattern.finditer(string):
        instructions.append(('dont', m.start()))

    # Sort instructions by their positions
    instructions.sort(key=lambda x: x[1])

    # Process instructions sequentially
    status = True  # Initially enabled
    total = 0
    for instr in instructions:
        if instr[0] == 'do':
            status = True
        elif instr[0] == 'dont':
            status = False
        elif instr[0] == 'mul':
            if status:
                x, y = instr[2]
                total += int(x) * int(y)
    return total

string = sys.stdin.read()
print(string)
print(multiply(string))

