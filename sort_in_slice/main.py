def reverse(arr, i, j):
    def helper(arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        helper(arr, left, mid)
        helper(arr, mid + 1, right)
        merge(arr, left, right)


    def merge(arr, m, n):
        if m >= n:
            return
        aux = []
        a = m
        mid = (m + n) // 2
        b = mid + 1
        while True:
            if arr[a] <= arr[b]:
                aux.append(arr[a])
                a += 1
                if a > mid:
                    for k in range(b, n + 1):
                        aux.append(arr[k])
                    break
            else:
                aux.append(arr[b])
                b += 1
                if b <= mid:
                    for k in range(a, mid + 1):
                        aux.append(arr[k])
                    break
        for item in aux:
            arr[m] = item
            m += 1


    helper(arr, i, j)


if __name__ == '__main__':
    arr = [3, 2, 6, 1, 7]
    reverse(arr, 0, 2)
    print(arr)
