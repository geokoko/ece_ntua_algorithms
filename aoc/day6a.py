import sys

grid = []
start_position = None
guard = ""
direction_map = {"^": 0, ">": 1, "v": 2, "<": 3}

def read_input():
    global start_position, grid, guard
    inp = sys.stdin.read().strip().split('\n')
    for row_idx, row in enumerate(inp):
        grid.append(row)
        for col_idx, char in enumerate(row):
            if char in direction_map:
                start_position = (row_idx, col_idx)
                guard = char

def simulate():
    global grid, start_position, guard

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()

    x, y = start_position
    facing = direction_map[guard]

    while 0 <= x <= len(grid) and 0 <= y <= len(grid[0]):
        visited.add((x, y))

        dx, dy = directions[facing]
        move_x, move_y = x + dx, y + dy

        if 0 <= move_x < len(grid) and 0 <= move_y < len(grid[0]) and grid[move_x][move_y] != "#":
            x, y = move_x, move_y
        elif move_x == len(grid) or move_y == len(grid[0]):
            return len(visited)
        else:
            facing = (facing + 1) % 4

    return len(visited)

if __name__ == "__main__":
    read_input()
    result = simulate()
    print(result)

