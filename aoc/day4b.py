def read_grid_from_input():
    """Reads multi-line input from the user and converts it into a 2D grid."""
    print("Please paste your grid below. End your input with an empty line:")
    grid_input = []
    while True:
        try:
            line = input()
            if line == "":
                break
            grid_input.append(line)
        except EOFError:
            break
    return grid_input

def is_valid_xmas(grid, x, y):
    """Checks if an X-MAS pattern exists centered at (x, y) in the grid."""
    n = len(grid)
    m = len(grid[0])
        # Check the "X" structure
    valid = 0
    try:
        sum = grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1]
        if (sum == 'SAM' or sum == 'MAS'):
            valid += 1
    except IndexError:
        pass

    try:
        sum = grid[x - 1][y + 1] + grid[x][y] + grid[x + 1][y - 1]
        if (sum == 'SAM' or sum == 'MAS'):
            valid += 1
    except IndexError:
        pass
    
    if valid == 2:
        return True
    
    return False

def count_xmas_patterns(grid):
    """Counts all occurrences of the X-MAS pattern in the grid."""
    n = len(grid)
    m = len(grid[0])
    count = 0

    for i in range(1, n - 1):  # Avoid boundaries
        for j in range(1, m - 1):  # Avoid boundaries
            if grid[i][j] == 'A' and is_valid_xmas(grid, i, j):
                count += 1

    return count

def main():
    grid = read_grid_from_input()
    total_xmas = count_xmas_patterns(grid)
    print(f"\nThe X-MAS pattern appears {total_xmas} times in the grid.")

if __name__ == "__main__":
    main()

