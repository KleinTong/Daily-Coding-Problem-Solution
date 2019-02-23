def make_partitions(x, arr):
    def exch(i, j):
        # print(arr, 'head_pos', head_pos, 'tail_pos', tail_pos, i)
        item = arr[i]
        arr[i] = arr[j]
        arr[j] = item


    head_pos = 0
    tail_pos = len(arr) - 1
    i = 0
    for i in range(len(arr)):
        if arr[i] > x and i < tail_pos:
            while True:
                if tail_pos == 0:
                    break
                if arr[tail_pos] > x:
                    tail_pos -= 1
                else:
                    if i < tail_pos:
                        exch(i, tail_pos)
                        tail_pos -= 1
                    break
        elif arr[i] < x and i > head_pos:
            while True:
                if head_pos == len(arr) - 1:
                    break
                if arr[head_pos] < x:
                    head_pos += 1
                else:
                    if i > head_pos:
                        exch(i, head_pos)
                        head_pos += 1
                    break
    return arr


if __name__ == '__main__':
    arr = [9, 12, -33, 5, 1, 14, -10, 10]
    print(make_partitions(1, arr))
    arr = [-1, -10, -10, -99, -1000]
    print(make_partitions(-7, arr))
    arr = [122, 333, 666, 222, 899]
    print(make_partitions(1, arr))
    arr = [9, 12, 3, 5, 14, 10, 10]
    print(make_partitions(10, arr))
