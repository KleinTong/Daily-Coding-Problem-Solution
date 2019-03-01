def sublist_sum(arr, i, j):
    def pre_processing(arr):
        result = {}
        cnt = 0
        result[(0, -1)] = 0
        for i in range(len(arr)):
            cnt += arr[i]
            result[(0, i)] = cnt
        cnt = 0
        for j in range(len(arr)-1, -1, -1):
            cnt += arr[j]
            result[(-1, j)] = cnt

        return result


    result = pre_processing(arr)
    total_cnt = result[(0, len(arr)-1)]
    i = i % len(arr)
    j = j % len(arr)
    return  total_cnt - result[(0, i-1)] - result[(-1, j)]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(sublist_sum(arr, 1, 3))
    print(sublist_sum(arr, 0, -1))
