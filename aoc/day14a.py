import os

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

def simulate_movement(positions, velocities, grid_width, grid_height):
    new_xs = [(p[0] + 100 * v[0]) % grid_width for p, v in zip(positions, velocities)]
    new_ys = [(p[1] + 100 * v[1]) % grid_height for p, v in zip(positions, velocities)]

    return new_xs, new_ys

def count_quadrants(new_xs, new_ys, grid_width, grid_height):
    top_left = top_right = bottom_left = bottom_right = 0

    for x, y in zip(new_xs, new_ys):
        if x == grid_width // 2 or y == grid_height // 2:
            continue
        if x < grid_width // 2 and y < grid_height // 2:
            top_left += 1
        elif x >= grid_width // 2 and y < grid_height // 2:
            top_right += 1
        elif x < grid_width // 2 and y >= grid_height // 2:
            bottom_left += 1
        elif x >= grid_width // 2 and y >= grid_height // 2:
            bottom_right += 1

    return top_left, top_right, bottom_left, bottom_right

if __name__ == "__main__":
    positions, velocities = read_input()
    print(positions)
    grid_width = 101
    grid_height = 103

    new_xs, new_ys = simulate_movement(positions, velocities, grid_width, grid_height)

    top_left, top_right, bottom_left, bottom_right = count_quadrants(new_xs, new_ys, grid_width, grid_height)
    print(top_left * top_right * bottom_left * bottom_right)

