def hops(arr):
    length = len(arr)

    def helper(index):
        if index == length-1:
            return True
        if index >= length:
            return False
        if arr[index] <= 0:
            return False
        return helper(index + arr[index])

    return helper(arr[0])


if __name__ == '__main__':
    arr = [2, 0, 1, 0]
    print(hops(arr))
    arr = [1, 1, 0, 1]
    print(hops(arr))
