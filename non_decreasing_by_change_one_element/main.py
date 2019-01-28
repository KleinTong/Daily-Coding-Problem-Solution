def main(arr):
    length = len(arr)
    cnt = 0
    for i in range(length):
        if i - 1 >= 0:
            if arr[i] < arr[i-1]:
                cnt += 1
                arr[i] = arr[i-1]
        if i + 1 < length:
            if arr[i] > arr[i+1]:
                cnt += 1
                arr[i] = arr[i+1]
        if cnt > 1:
            return False
    return True


if __name__ == '__main__':
    arr = [10, 5, 7, 7, 1]
    print(main(arr))
