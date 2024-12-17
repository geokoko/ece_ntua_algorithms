import sys
from typing import List, Dict
from functools import cmp_to_key

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

def isValid(update: List[int], rules: Dict) -> bool:
    seen = set()
    for page in update:
        if page in rules:
            for after_page in rules[page]:
                if after_page in seen:
                    return False
        seen.add(page)
    return True

def sort_updates(update: List[int], rules: Dict) -> List:
    def comparator(page1, page2):
        if page1 in rules and page2 in rules[page1]:
            return -1
        if page2 in rules and page1 in rules[page2]:
            return 1
        return 0

    return sorted(update, key=cmp_to_key(comparator))

if __name__ == "__main__":
    rules, updates = read_input()
    middle_pages = []
    for update in updates:
        if not isValid(update, rules):
            new_update = sort_updates(update, rules)
            n = len(new_update)
            middle = new_update[n // 2]
            middle_pages.append(middle)

    print(sum(middle_pages))
