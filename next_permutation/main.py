def next_greater(arr):
    def exch(n_arr, i, j):
        item = n_arr[i]
        n_arr[i] = n_arr[j]
        n_arr[j] = item


    def reverse_arr(n_arr):
        result = []
        for i in range(len(n_arr) - 1, -1, -1):
            result.append(n_arr[i])
        return result


    length = len(arr)
    for i in range(length - 2, -1, -1):
        if arr[i] < arr[i+1]:
            exch(arr, i, i+1)
            print(arr)
            return arr
    print(reverse_arr(arr))


if __name__ == '__main__':
    arr = [1, 2, 3]
    arr = [3, 2, 1]
    arr = [3, 4, 5]
    arr = [3, 5, 4]
    next_greater(arr)
