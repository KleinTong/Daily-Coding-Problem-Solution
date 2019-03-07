def find_majority(arr):
    arr.sort()
    return arr[len(arr)//2 - 1]


if __name__ == '__main__':
    arr = [1, 2, 1, 1, 3, 4, 0]
    print(find_majority(arr))
    arr = [1, 1, 5, 2, 4, 1]
    print(find_majority(arr))
