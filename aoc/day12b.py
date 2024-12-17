import os
from collections import deque

example = os.path.join(os.path.dirname(__file__), 'example.txt')
input = os.path.join(os.path.dirname(__file__), 'input.txt')

chosen = input

def read_input():
    with open(chosen) as f:
        lines = f.read().strip().split('\n')
        grid = [list(row) for row in lines]

        for row in grid:
            print(row)

    return grid

def group_regions(grid):
    regions = []

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

    def value(grid, x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return grid[x][y]
        else:
            return ' '

    def find_region(i, j, grid):
        queue = deque([(i, j)])
        visited.add((i, j))
        plant_type = grid[i][j]
        area = 0
        perimeter = 0
        corners = 0
        cells = [] # what to return

        while queue:
            i, j = queue.popleft()
            area += 1
            cells.append((i, j))

            neighbors = [
                    (i - 1, j, value(grid, i - 1, j)),  # Up
                    (i, j + 1, value(grid, i, j + 1)),  # Right
                    (i + 1, j, value(grid, i + 1, j)),  # Down
                    (i, j - 1, value(grid, i, j - 1))   # Left
                ]

            for k, (ni, nj, neighbor_val) in enumerate(neighbors):
                if neighbor_val != plant_type:
                    perimeter += 1

                next_k = (k + 1) % 4 # turn right
                if neighbors[k][2] != plant_type and neighbors[next_k][2] != plant_type:
                    print("Convex corner at", plant_type, "at", i, j)
                    corners += 1   # check if this is a convex corner

            diagonal_neighbors = [
                (i - 1, j - 1, value(grid, i - 1, j - 1)),  # Up-Left
                (i - 1, j + 1, value(grid, i - 1, j + 1)),  # Up-Right
                (i + 1, j - 1, value(grid, i + 1, j - 1)),  # Down-Left
                (i + 1, j + 1, value(grid, i + 1, j + 1))   # Down-Right
                ]

            # checking for non convex corners
            for x, y, val in diagonal_neighbors:
                if val != plant_type and value(grid, i, y) == plant_type and value(grid, x, j) == plant_type:
                    print("Non-convex corner at", plant_type, "at", i, j)
                    corners += 1

            for ni, nj, neighbor_val in neighbors:
                if neighbor_val == plant_type and (ni, nj) not in visited:
                    queue.append((ni, nj))
                    visited.add((ni, nj))

        return plant_type, area, perimeter, corners, cells

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited: # if not visited, new region must be defined
                plant_type, total_area, total_perimeter, corners, cells = find_region(i, j, grid) # find region starting from this cell
                regions.append({"plant_type": plant_type, "total_area": total_area, "total_perimeter": total_perimeter, "cells": cells,
                                "price_tag": corners * total_area, "corners": corners})

    return regions

if __name__ == '__main__':
    grid = read_input()
    regions = group_regions(grid)
    print(sum(region["price_tag"] for region in regions))

