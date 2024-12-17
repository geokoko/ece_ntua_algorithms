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

left_list.sort()
right_list.sort()

total = 0 

for i, j in zip(left_list, right_list):
    dist = abs(i - j)
    total += dist

print(total)
