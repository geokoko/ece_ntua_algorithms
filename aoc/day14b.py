import os
from time import sleep

example = os.path.join(os.path.dirname(__file__), "example.txt")
input = os.path.join(os.path.dirname(__file__), "input.txt")

def read_input():
    with open(input) as file:
        lines = file.read().strip().split("\n")
        positions = []
        velocities = []

        for line in lines:
            parts = line.split()
            p = tuple(map(int, parts[0][2:].split(',')))
            v = tuple(map(int, parts[1][2:].split(',')))
            positions.append(p)
            velocities.append(v)

    return positions, velocities

def move(positions, velocities, grid_width=101, grid_height=103):
    copy_positions = positions.copy()
    copy_velocities = velocities.copy()
    count = 0

    """
    Trying to implement a heuristic to detect if the robots are forming a tree...
    """

    def is_tree(new_xs, new_ys):
        from statistics import mean

        x_center = round(mean(new_xs))
        y_center = round(mean(new_ys))

        rows = {}
        for x, y in zip(new_xs, new_ys):
            if y not in rows:
                rows[y] = []
            rows[y].append(x)

        sorted_rows = sorted(rows.items())

        prev_width = 0
        for y, x_coords in sorted_rows:
            x_coords.sort()

            for i in range(len(x_coords) // 2):
                if x_coords[i] != 2 * x_center - x_coords[-(i + 1)]:
                    return False

            row_width = len(x_coords)
            if row_width < prev_width:
                return False
            prev_width = row_width

        trunk_rows = sorted_rows[-2:]  # Last 2 rows
        for _, x_coords in trunk_rows:
            if not all(x == x_center for x in x_coords):
                return False

        return True


    while True:
        """
        Move the robots to the new positions for each second
        """
        new_xs = []
        new_ys = []
        for p, v in zip(copy_positions, copy_velocities):
            x, y = p
            vx, vy = v
            new_xs.append((x + vx) % grid_width)
            new_ys.append((y + vy) % grid_height)

        count += 1
        print_grid(new_xs, new_ys, grid_width, grid_height)
        print(count)

        new_positions = list(zip(new_xs, new_ys))
        if new_positions == positions:
            print("ITERATION FINISHED!!!!!!!!! INITIAL POSITIONS REACHED")
            return count
        if is_tree(new_xs, new_ys):
            print("ITERATION FINISHED!!!!!!!!! TREE DETECTED")
            return count

        copy_positions = list(zip(new_xs, new_ys))

def print_grid(new_xs, new_ys, grid_width, grid_height):
    grid = [[' ' for _ in range(grid_width)] for _ in range(grid_height)]

    for x, y in zip(new_xs, new_ys):
        grid[y][x] = '.'

    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

    print("+" + "-" * (grid_width - 2) + "+")

if __name__ == "__main__":
    positions, velocities = read_input()
    grid_width = 101
    grid_height = 103

    print(move(positions, velocities))
