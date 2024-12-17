import sys
from itertools import combinations

def read_input():
    grid = []
    antennas = {}
    inp = sys.stdin.read().strip().split('\n')
    for row_idx, row in enumerate(inp):
        grid.append(row)
        for col_idx, char in enumerate(row):
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((row_idx, col_idx))

    return grid, antennas

def find_antinodes(grid, antennas):
    rows = len(grid)
    cols = len(grid[0])
    anti_nodes = {}

    for char, nodes in antennas.items():
        for (x1, y1), (x2, y2) in combinations(nodes, 2):
            dx = x2 - x1
            dy = y2 - y1

            antinode1 = (x1 - dx, y1 - dy)
            antinode2 = (x2 + dx, y2 + dy)

            for antinode in [antinode1, antinode2]:
                if (
                    0 <= antinode[0] < rows and 
                    0 <= antinode[1] < cols and 
                    grid[antinode[1]][antinode[0]] == ".") :
                        if antinode not in anti_nodes:
                            anti_nodes[antinode] = []
                        anti_nodes[antinode].append(((x1, y1), (x2, y2)))

    print(f"All antinodes (with duplicates): {anti_nodes}")
    return anti_nodes

def build_new_grid(grid, anti_nodes):
    new_grid = []
    for row_idx, row in enumerate(grid):
        new_row = []
        for col_idx, char in enumerate(row):
            if (row_idx, col_idx) in anti_nodes:
                new_row.append("#")
            elif grid[row_idx][col_idx] != ".":
                new_row.append(grid[row_idx][col_idx])
            else:
                new_row.append(".")
        new_grid.append("".join(new_row))

    return new_grid

if __name__ == "__main__":
    grid, antennas = read_input()
    anti_nodes = find_antinodes(grid, antennas)
    print(len(anti_nodes))
    new_grid = build_new_grid(grid, anti_nodes)
    print("\n".join(new_grid))
