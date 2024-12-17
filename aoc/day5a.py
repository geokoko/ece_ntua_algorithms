import sys
from typing import List

def read_input():
    input_lines = sys.stdin.read().strip().split("\n")
    
    # Split into rules and updates based on an empty line
    split_index = input_lines.index("")  # Find the separator (empty line)
    rules_lines = input_lines[:split_index]
    updates_lines = input_lines[split_index + 1:]
    
    # Parse rules into a dictionary
    rules = {}
    for line in rules_lines:
        before, after = map(int, line.split("|"))
        if before not in rules:
            rules[before] = set()
        rules[before].add(after)
    
    # Parse updates into a list of lists of integers
    updates = []
    for line in updates_lines:
        updates.append(list(map(int, line.split(","))))
    
    return rules, updates

def isValid(update: List[int], rules: dict) -> bool:
    seen = set()
    for page in update:
        if page in rules:
            for after_page in rules[page]:
                if after_page in seen:
                    return False
        seen.add(page)
    return True

if __name__ == "__main__":
    rules, updates = read_input()
    middle_pages = []
    for update in updates:
        if isValid(update, rules):
            n = len(update)
            middle = update[n // 2]
            middle_pages.append(middle)

    print(sum(middle_pages))
