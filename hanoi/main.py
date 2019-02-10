def hanoi(n):
    def helper(k, start, destination, rest):
        if k == 0:
            return
        helper(k-1, start, rest, destination)
        print('Move', str(k) + 'th', 'to', destination)
        helper(k-1, rest, destination, start)


    helper(n, '1', '3', '2')


if __name__ == '__main__':
    hanoi(10)
