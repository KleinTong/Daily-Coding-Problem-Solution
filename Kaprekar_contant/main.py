def kaprekar(n):
    def get_digit(item):
        i = item
        digits = []
        while i > 0:
            digits.append(i % 10);
            i //= 10;
        return digits;


    def min_maker(item):
        return sorted(get_digit(item))


    def max_maker(item):
        return sorted(get_digit(item), reverse=True)


    def decimal_maker(arr):
        result = 0
        for i in arr:
            result = result * 10 + i;
        return result


    steps = 0
    item = n
    while True:
        max_num = decimal_maker(max_maker(item))
        min_num = decimal_maker(min_maker(item))
        item = max_num - min_num
        steps += 1
        if item == 6174:
            return steps


if __name__ == '__main__':
    n = 1234
    print(kaprekar(n))
    n = 7823
    print(kaprekar(n))
