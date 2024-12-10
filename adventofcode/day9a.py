import os

input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')

def read():
    with open(input_file, 'r') as f:
        disk = f.read().strip()
    image = []

    for idx in range(len(disk)):
        char = idx // 2 if idx % 2 == 0 else '.'
        image.extend([char] * int(disk[idx]))

    return image

def recreate(image):
    image = list(image)
    while True:
        try:
            left_free_idx = image.index('.')
        except ValueError:
            break

        right_file_idx = None

        for i in range(len(image) - 1, -1, -1):
            if isinstance(image[i], int):
                right_file_idx = i
                break

        if right_file_idx is None or right_file_idx <= left_free_idx:
            break

        image[left_free_idx], image[right_file_idx] = image[right_file_idx], '.'

    while '.' in image:
        image.remove('.')

    return image

def calculate_checksum(image):
    return sum(i*j for i, j in enumerate(image))

if __name__ == '__main__':
    disk_image = read()
    disk_image_str = recreate(disk_image)
    checksum = calculate_checksum(disk_image_str)
    print(checksum)
