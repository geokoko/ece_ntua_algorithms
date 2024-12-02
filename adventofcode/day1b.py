import sys

left_list = []
right_list = []

for line in sys.stdin:
    parts = line.strip().split()

    if len(parts) == 2:    
        try:
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))
        except ValueError:
            print("Invalid input")
            break
    else:
        print("Invalid input")

from collections import Counter

right_counts = Counter(right_list)

similar = 0

for left in left_list:
    count_in_right = right_counts.get(left, 0)
    similar += left * count_in_right

print(similar)
