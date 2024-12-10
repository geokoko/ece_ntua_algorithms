import os

file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')

def read_input():
    graph = []
    with open(file, 'r') as f:
        for line in f:
            graph.append(list(map(int, line.strip('\n'))))

    return graph

def solve(graph):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up
    start_positions = []
    total = 0

    for i, row in enumerate(graph):
        for j, value in enumerate(row):
            if value == 0:
                start_positions.append((i, j, value)) # point (i, j)

    for start_position in start_positions:
        stack = [start_position]  
        visited = set()
        reachable_nines = set()

        while stack:
            i, j, value = stack.pop()
            visited.add((i, j))

            for dir in directions:
                ni, nj = i + dir[0], j + dir[1]

                if (0 <= ni < len(graph) and 0 <= nj < len(graph[0])) and (ni, nj) not in visited:
                    if graph[ni][nj] == value + 1:
                        stack.append((ni, nj, graph[ni][nj]))

            if value == 9:
                reachable_nines.add((i, j))

        total += len(reachable_nines)

    return total

if __name__ == '__main__':
    graph = read_input()
    print(solve(graph))
