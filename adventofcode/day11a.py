from collections import Counter
from typing import Optional
from math import log10

def read_input() -> Counter:
    with open("input.txt", "r") as file:
        line = file.readline().strip()
        stones = Counter(map(int, line.split()))
    return stones

def count_digits(n: int) -> int:
    if n == 0:
        return 1  # Special case: log10(0) is undefined
    return int(log10(abs(n))) + 1

def simulate_stones(stones: Optional[Counter] = None, blinks: int = 0) -> Counter:
    for blink in range(blinks):
        new_stones = Counter()
        for stone, freq in stones.items():
            if stone == 0:
                new_stones[1] += freq
            elif count_digits(stone) % 2 == 0:
                s = str(stone)
                mid = len(s) // 2
                left = int(s[:mid])
                right = int(s[mid:])
                new_stones[left] += freq
                new_stones[right] += freq
            else:
                new_stones[stone * 2024] += freq
        stones = new_stones

    return stones

if __name__ == "__main__":
    stones = read_input()
    ans = simulate_stones(stones, 75)
    print(sum(ans.values()))
