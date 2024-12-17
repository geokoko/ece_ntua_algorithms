import os

example = os.path.join(os.path.dirname(__file__), 'example.txt')
input = os.path.join(os.path.dirname(__file__), 'input.txt')

def read_input():
    data = []
    with open(input, 'r') as f:
        blocks = f.read().strip().split('\n\n')
        for block in blocks:
            lines = block.strip().split('\n')
            print(lines)
            x_A, y_A = map(int, lines[0].split(':')[1].strip().replace('X+', '').replace('Y+', '').split(','))
            x_B, y_B = map(int, lines[1].split(':')[1].strip().replace('X+', '').replace('Y+', '').split(','))
            x_T, y_T = map(int, lines[2].split(':')[1].strip().replace('X=', '').replace('Y=', '').split(','))

            data.append({
                'A': (x_A, y_A),
                'B': (x_B, y_B),
                'target': (x_T, y_T)
                })

        return data

def solve(data, max_presses=10000000000):
    tokens_cost = 0

    for vals in data:
        x_A, y_A = vals['A']
        x_B, y_B = vals['B']
        x_T, y_T = vals['target']

        min_cost = float('inf')
        solution_found = False

        for i in range(max_presses + 1):
            for j in range(max_presses + 1):
                x = x_A * i + x_B * j
                y = y_A * i + y_B * j
                if x == x_T and y == y_T:
                    cost = 3 * i + j
                    if cost < min_cost:
                        min_cost = cost
                        solution_found = True
                        break

        if solution_found:
            tokens_cost += min_cost

    return tokens_cost

if __name__ == '__main__':
    data = read_input()
    print(solve(data))
