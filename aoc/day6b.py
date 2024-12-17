import sys

grid = []
start_position = None
guard = ""
direction_map = {"^": 0, ">": 1, "v": 2, "<": 3}

def read_input():
    global start_position, grid, guard
    inp = sys.stdin.read().strip().split('\n')
    for row_idx, row in enumerate(inp):
        grid.append(list(row))  
        for col_idx, char in enumerate(row):
            if char in direction_map:
                start_position = (row_idx, col_idx)
                guard = char

def simulate_with_obstacle(obst_x, obst_y):
    original_char = grid[obst_x][obst_y]
    grid[obst_x][obst_y] = 'O'

    result = simulate_guard_movement()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = "")
        print("")
    print(result)
    print("")

    grid[obst_x][obst_y] = original_char
    return result

def simulate_guard_movement():
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    x, y = start_position
    facing = direction_map[guard]
    visited_states = set()

    for _ in range(100000): 
        state = (x, y, facing)
        if state in visited_states:
            return True
        visited_states.add(state)
        
        dx, dy = directions[facing]
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] not in ['#', 'O']:
            x, y = nx, ny
        elif not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
            return False
        else:
            facing = (facing + 1) % 4

    return False

if __name__ == "__main__":
    read_input()

    loop_count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == start_position:
                continue
            if grid[i][j] == '.':
                if simulate_with_obstacle(i, j):
                    loop_count += 1

    print(loop_count)

