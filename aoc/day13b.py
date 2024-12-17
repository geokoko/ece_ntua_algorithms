import os

example = os.path.join(os.path.dirname(__file__), 'example.txt')
input = os.path.join(os.path.dirname(__file__), 'input.txt')

def read_input():
    data = []
    with open(input, 'r') as f:
        blocks = f.read().strip().split('\n\n')
        for block in blocks:
            lines = block.strip().split('\n')
            x_A, y_A = map(int, lines[0].split(':')[1].strip().replace('X+', '').replace('Y+', '').split(','))
            x_B, y_B = map(int, lines[1].split(':')[1].strip().replace('X+', '').replace('Y+', '').split(','))
            x_T, y_T = map(int, lines[2].split(':')[1].strip().replace('X=', '').replace('Y=', '').split(','))

            data.append({
                'A': (x_A, y_A),
                'B': (x_B, y_B),
                'target': (x_T + 10000000000000, y_T + 10000000000000)
                })

        return data

def solve(data, max_presses=100):
    tokens_cost = 0

    for vals in data:
        x_A, y_A = vals['A']
        x_B, y_B = vals['B']
        x_T, y_T = vals['target']

        det = x_A * y_B - x_B * y_A
        if det == 0:
            continue

        det_A = x_T * y_B - x_B * y_T
        det_B = x_A * y_T - x_T * y_A

        if det_A % det != 0 or det_B % det != 0:
            continue

        solA = det_A // det
        solB = det_B // det

        if solA < 0 or solB < 0:
            continue

        tokens_cost += 3 * solA + solB

    return tokens_cost

if __name__ == '__main__':
    data = read_input()
    print(solve(data))
