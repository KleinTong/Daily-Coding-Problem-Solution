from random import randint

def rand5():
    return randint(1, 5)


def rand7():
    max = -1
    pos = []
    for i in range(1, 8):
        num = rand5()
        if max < num:
            pos = [i]
            max = num
        elif max == num:
            pos.append(i)

    while len(pos) > 1:
        aux_max = -1
        aux = []
        for i in range(len(pos)):
            num = rand5()
            if num > aux_max:
                aux_max = num
                aux = [pos[i]]
            elif num == aux_max:
                aux.append(pos[i])
        # pos = [pos[i] for i in aux]
        pos = aux

    return pos[0]


if __name__ == '__main__':
    a = [i for i in range(1, 8)]
    b = [0 for i in range(1, 8)]
    result = dict(zip(a, b))
    result_2 = result.copy()
    for _ in range(1000000):
        result[rand7()] += 1
        result_2[randint(1, 7)] += 1
    print(result)
    print(result_2)
