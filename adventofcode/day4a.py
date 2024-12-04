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
    grid = [list(row) for row in grid_input]
    return grid

def get_all_directions(grid):
    """Generates all possible lines in the grid where words can occur."""
    rows, cols = len(grid), len(grid[0])
    lines = []

    # Horizontal lines
    for row in grid:
        lines.append(''.join(row))          # Left to right
        lines.append(''.join(row[::-1]))    # Right to left

    # Vertical lines
    for col in range(cols):
        col_vals = [grid[row][col] for row in range(rows)]
        lines.append(''.join(col_vals))          # Top to bottom
        lines.append(''.join(col_vals[::-1]))    # Bottom to top

    # Diagonals (\ direction)
    for p in range(-rows + 1, cols):
        diag = [grid[i][i - p] for i in range(max(0, p), min(rows, cols + p))]
        if diag:
            lines.append(''.join(diag))          # Top-left to bottom-right
            lines.append(''.join(diag[::-1]))    # Bottom-right to top-left

    # Diagonals (/ direction)
    for p in range(rows + cols - 1):
        diag = [grid[i][p - i] for i in range(max(0, p - cols + 1), min(rows, p + 1)) if 0 <= p - i < cols]
        if diag:
            lines.append(''.join(diag))          # Top-right to bottom-left
            lines.append(''.join(diag[::-1]))    # Bottom-left to top-right

    return lines

def count_word_occurrences(lines, word):
    """Counts how many times the word occurs in the list of lines."""
    count = 0
    for line in lines:
        idx = line.find(word)
        while idx != -1:
            count += 1
            idx = line.find(word, idx + 1)
    return count

def main():
    word = "XMAS"
    grid = read_grid_from_input()
    lines = get_all_directions(grid)
    total_occurrences = count_word_occurrences(lines, word)
    print(f"\nThe word '{word}' occurs {total_occurrences} times in the grid.")

if __name__ == "__main__":
    main()

