def nearest_larger(arr, i):
    length = len(arr)
    record = [-1 for _ in range(length)]
    for m in range(length):
        for n in range(m, length):
            if arr[m] > arr[n]:
                record[n] = m

    for k in range(length - 1, -1, -1):
        for j in range(k, -1, -1):
            if arr[k] > arr[j]:
                if record[j] == -1:
                    record[j] = k
                else:
                    if abs(record[j] - j) > abs(k -j):
                        record[j] = k

    return record[i]


if __name__ == '__main__':
    arr = [4, 7, 3, 11, 6, 10]
    print(nearest_larger(arr, 0))
    print(nearest_larger(arr, 4))
    print(nearest_larger(arr, 2))
