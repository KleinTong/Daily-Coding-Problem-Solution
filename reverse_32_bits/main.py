def reverse(num):
    x = 0xFFFFFFFF
    return x - num


if __name__ == '__main__':
    x = 1
    x = 0b11110000111100001111000011110000
    print(reverse(x))
    y = 0b00001111000011110000111100001111
    print(y)
