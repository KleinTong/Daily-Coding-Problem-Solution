def sum(arr, n):
    def helper(start, end, num):
        if num > n:
            return None
        if num == n:
            return arr[start:end]
        if end >= len(arr):
            return None
        num += arr[end]
        return helper(start, end + 1, num)


    for i in range(len(arr)):
        result = helper(i, i, 0)
        if result:
            return result
    return None


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(sum(arr, 10))
