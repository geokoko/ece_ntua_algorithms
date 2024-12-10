import os

input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
#input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'example.txt')
def read():
    with open(input_file, 'r') as f:
        disk = f.read().strip()
    files = []
    buckets = []

    pos = 0
    for idx in range(len(disk)):
        size = int(disk[idx]) # size of file or bucket
        
        if idx % 2 == 0:
            files.append((idx // 2, pos, size)) # (file_id, fpos, size)
        else:
            buckets.append((pos, size)) # (bpos, size)
        pos += size

    return files, buckets

def recreate(files, buckets):
    # 00...111...2...333.44.5555.6666.777.888899
    for fidx in range(len(files) - 1, -1, -1):
        fid, fpos, fsize = files[fidx]

        if fsize == 0:
            continue

        for i in range(len(buckets)):
            bpos, bsize = buckets[i]

            if fsize <= bsize and bpos + bsize <= fpos:
                files[fidx] = (fid, bpos, fsize) # change fpos
                buckets[i] = (bpos + fsize, bsize - fsize) # resizing bucket
                break

    print(files)

    return files

def calculate_checksum(files):
    return sum([fid * (fpos + i) for fid, fpos, fsize in files for i in range(fsize)])

if __name__ == '__main__':
    files, buckets = read()
    new_files = recreate(files, buckets)
    checksum = calculate_checksum(new_files)
    print(checksum)
