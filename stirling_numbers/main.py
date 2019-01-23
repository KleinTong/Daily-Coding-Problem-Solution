def stirling(n, k):
    if k > n:
        raise ValueError('wrong k')
    def helper(rest, d):
        if not rest:
            for value in d.values():
                if not value:
                    return 0
            # print(d)
            return 1
        num = rest[0]
        result = 0
        for key in d.keys():
            d[key].append(num)
            result += helper(rest[1:], d)
            d[key].remove(num)
        return result


    num_arr = [i for i in range(1, n+1)]
    host = [[] for _ in range(k)]
    d = dict(zip(num_arr, host))
    repeat = 1
    for i in range(1, k+1):
        repeat *= i
    # print(repeat)
    return helper(num_arr, d) // repeat


if __name__ == '__main__':
    print(stirling(9, 4))
    print(stirling(9, 3))
    print(stirling(9, 6))
