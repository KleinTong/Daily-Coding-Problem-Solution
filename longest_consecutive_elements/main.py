def longest(arr):
    arr.sort()
    length = 0
    part_len = 1
    for i in range(len(arr)-1):
        if arr[i] + 1 == arr[i+1]:
            part_len += 1
        else:
            if part_len > length:
                length = part_len
            part_len = 1
    return length


if __name__ == '__main__':
    arr = [100, 4, 200, 1, 3, 2, 5]
    print(longest(arr))
