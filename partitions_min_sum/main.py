def make_min_sum(arr, k):
    result = [[] for i in range(k)]
    cnts = [0 for i in range(k)]
    for item in reversed(sorted(arr)):
        index = -1
        min = float('inf')
        for i in range(k):
            cnt = cnts[i] + item
            if cnt < min:
                min = cnt
                index = i
        result[index].append(item)
        cnts[index] = min
    print(result)
    return sorted(cnts)[-1]


if __name__ == '__main__':
    N = [5, 1, 2, 7, 3, 4]
    k = 3
    print(make_min_sum(N, k))
    N = [5, 4, 3, 1, 3, 7]
    k = 3
    print(make_min_sum(N, k))
