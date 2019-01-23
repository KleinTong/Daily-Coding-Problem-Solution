def swap(i):
    odd  = int('0b10101010', 2)
    even = int('0b01010101', 2)
    num_1 = (i & odd) // 2
    num_2 = (i & even) * 2
    return num_1 + num_2


def bonus_swap(i):
    return ((i & 170) >> 1) + ((i & 85) << 1)

if __name__ == '__main__':
    num = 17
    print(swap(num))
    print(bonus_swap(num))
