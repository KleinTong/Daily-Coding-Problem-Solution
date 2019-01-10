def fib(n):
    arr = [-1 for _ in range(n+1)]


    def helper(i):
        if i <= 0:
            return 0
        if i == 1:
            return 1
        if arr[i] > -1:
            return arr[i]
        arr[i] = helper(i-1) + helper(i-2)
        return arr[i]


    return helper(n)


if __name__ == '__main__':
    print(fib(40))
