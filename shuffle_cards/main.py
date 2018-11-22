from random import randint


def rand_num(k):
    return randint(0, k)


def shuffle(arr):
    def exch(i, j):
        item = arr[i]
        arr[i] = arr[j]
        arr[j] = item


    for i in range(len(arr) - 1, -1, -1):
        index = rand_num(i)
        exch(index, i)


if __name__ == '__main__':
    arr = [i for i in range(10)]
    print(arr)
    shuffle(arr)
    print(arr)
