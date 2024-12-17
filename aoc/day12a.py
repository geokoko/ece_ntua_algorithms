import os
from collections import deque

example = os.path.join(os.path.dirname(__file__), 'example.txt')
input = os.path.join(os.path.dirname(__file__), 'input.txt')

chosen = example

def read_input():
    with open(chosen) as f:
        lines = f.read().strip().split('\n')
        grid = [list(row) for row in lines]

    return grid

def group_regions(grid):
    regions = []

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

    def find_region(i, j, grid):
        queue = deque([(i, j)])
        visited.add((i, j))
        plant_type = grid[i][j]
        area = 0
        perimeter = 0
        cells = [] # what to return

        while queue:
            i, j = queue.popleft()
            area += 1
            cells.append((i, j))
            
            for dir in directions:
                ni = i + dir[0]
                nj = j + dir[1]

                if 0 <= ni < rows and 0 <= nj < cols:
                    if (ni, nj) not in visited and grid[ni][nj] == plant_type:
                        queue.append((ni, nj))
                        visited.add((ni, nj))
                    elif grid[ni][nj] != plant_type:
                        perimeter += 1
                else:
                    perimeter += 1

        return plant_type, area, perimeter, cells

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited: # if not visited, new region must be defined
                plant_type, total_area, total_perimeter, cells = find_region(i, j, grid) # find region starting from this cell
                regions.append({"plant_type": plant_type, "total_area": total_area, "total_perimeter": total_perimeter, "cells": cells,
                                "price_tag": total_area * total_perimeter})

    return regions

if __name__ == '__main__':
    grid = read_input()
    print(grid)
    regions = group_regions(grid)
    print(sum(region["price_tag"] for region in regions))

