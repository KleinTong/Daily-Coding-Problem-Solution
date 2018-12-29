def division(a, b):
    if a < 0 or b < 0:
        raise ValueError('negative number not allowed')
    left = a
    right = b
    quotient = 0
    while left >= right:
        left -= right
        quotient += 1
    return quotient


if __name__ == '__main__':
    a = 66
    b = 3
    print(division(a, b))
