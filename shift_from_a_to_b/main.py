def shift(a, b):
    i = b.index(a[0])
    s = b[i:] + b[0:i]
    return s == a


if __name__ == '__main__':
    a = 'abcde'
    b = 'cdeab'
    print(shift(a, b))
    a = 'abc'
    b = 'acb'
    print(shift(a, b))
