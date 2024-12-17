import sys

def is_safe(levels):
    diffs = []
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        if diff == 0:
            return False  
        if not (1 <= abs(diff) <= 3):
            return False  
        diffs.append(diff)

    if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
        return True
    else:
        return False


count = 0
reports = []
for line in sys.stdin:
    line_list = list(map(int, line.strip().split()))
    reports.append(line_list)

for report in reports:
    if is_safe(report):
        count += 1

print(count)
