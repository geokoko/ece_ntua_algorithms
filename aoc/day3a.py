import re
import sys

def multiply(string):
    pattern = r"mul\((\d+),(\d+)\)"
    match = re.findall(pattern, string)

    total = 0
    for x,y in match:
        total += int(x)*int(y)

    return total

string=sys.stdin.read()

print(string)
print(multiply(string))
