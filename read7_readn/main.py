def read7(f_buf):
    item = f_buf[0:7]
    f_buf[:] = f_buf[7:]
    return ''.join(item)


def readN(f_buf, n):
    def helper(i):
        if i < 7:
            f_buf[:] = (7 - i) * ['0'] + f_buf[:]
            return (read7(f_buf))[7-i:7]
        else:
            return read7(f_buf) + helper(i - 7)


    return helper(n)


if __name__ == '__main__':
    filename = 'content.txt'
    f = open(filename, 'r')
    f_buf = list(f.read())
    while f_buf:
        # result = read7(f_buf)
        result = readN(f_buf, 15)
        print(repr(result))
    # print(readN(f_buf, 9))
