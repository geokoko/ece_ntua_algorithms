import os

file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')

def read_input():
    graph = []
    with open(file, 'r') as f:
        for line in f:
            graph.append(list(map(int, line.strip('\n'))))
    return graph

def compute_score_and_rating(graph):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    scores = []
    ratings = []

    start_positions = [(i, j) for i in range(len(graph)) for j in range(len(graph[0])) if graph[i][j] == 0]

    def dfs(i, j, value, path, reachable_nines, distinct_trails):
        if value == 9:
            reachable_nines.add((i, j))  # Unique positions for score
            distinct_trails.add(tuple(path))  # Distinct trails for rating
            return

        for dir in directions:
            ni, nj = i + dir[0], j + dir[1]
            if (
                0 <= ni < len(graph)
                and 0 <= nj < len(graph[0])
                and (ni, nj) not in path  # Prevent revisiting
                and graph[ni][nj] == value + 1
            ):
                dfs(ni, nj, graph[ni][nj], path + [(ni, nj)], reachable_nines, distinct_trails)

    for start_position in start_positions:
        reachable_nines = set()  # For score
        distinct_trails = set()  # For rating
        dfs(start_position[0], start_position[1], 0, [start_position], reachable_nines, distinct_trails)
        scores.append(len(reachable_nines))  # Number of unique 9s
        ratings.append(len(distinct_trails))  # Number of distinct trails

    return scores, ratings

if __name__ == '__main__':
    graph = read_input()
    scores, ratings = compute_score_and_rating(graph)
    print("Trailhead Scores:", scores)
    print("Trailhead Ratings:", ratings)
    print("Total Score:", sum(scores))
    print("Total Rating:", sum(ratings))

