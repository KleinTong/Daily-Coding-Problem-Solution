def rotate(arr, k):
    def exch(i, j):
        item = arr[i]
        arr[i] = arr[j]
        arr[j] = item


    def first_move(i):
        target = (length + i - k) % length
        exch(i, target)


    def second_move(i):
        j = i
        cnt = 0
        while cnt < length - 2 * k:
            exch(j, j+1)
            j += 1
            cnt += 1


    length = len(arr)
    for i in range(k-1, -1, -1):
        first_move(i)

    for i in range(k-1, -1, -1):
        second_move(i)

    for i in range(length):
        print(arr[i], end=' ')
    print()


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rotate(arr, 4)
    length = len(arr)
    for i in range(length):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        rotate(arr, i)
