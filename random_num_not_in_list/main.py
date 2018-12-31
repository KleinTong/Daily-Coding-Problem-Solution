from random import randint


def random_generator(n, arr):
    opt_arr = [i for i in range(n)]
    final_arr = []

    for num in opt_arr:
        if num not in arr:
            final_arr.append(num)
    length = len(final_arr)


    def helper():
        nonlocal final_arr
        i = randint(0, length-1)
        return final_arr[i]


    return helper


if __name__ == '__main__':
    arr = [1, 3]
    g = random_generator(10, arr)
    for _ in range(30):
        print(g())
