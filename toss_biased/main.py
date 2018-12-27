from random import randint


def toss_biased():
    i = randint(1, 10)

    def helper():
        nonlocal i
        j = randint(1, 10)
        # print('i is', i, 'j is', j)
        if j < i:
            return 1
        else:
            return 0


    return helper


def toss_unbiased(toss):
    def helper():
        result = ''
        for _ in range(2):
            result += str(toss())
        if result == '10':
            return 0
        elif result == '01':
            return 1
        elif result == '00':
            cnt = 0
            while True:
                if toss() == 1:
                    if cnt % 2 == 0:
                        return 1
                    else:
                        return 0
                cnt += 1
        elif result == '11':
            cnt = 0
            while True:
                if toss() == 0:
                    if cnt % 2 == 1:
                        return 1
                    else:
                        return 0
                cnt += 1


    return helper

if __name__ == '__main__':
    zero_cnt = 0
    one_cnt = 0
    stan_zero = 0
    stan_one = 0
    total_cnt = 0

    toss = toss_biased()
    u_toss = toss_unbiased(toss)
    for _ in range(2000000):
        result = u_toss()
        total_cnt += 1
        if result == 0:
            zero_cnt += 1
        elif result == 1:
            one_cnt += 1
        m = randint(0, 1)
        if m == 0:
            stan_zero += 1
        elif m == 1:
            stan_one += 1
    print('one:', one_cnt, one_cnt / total_cnt)
    print('zero:', zero_cnt, zero_cnt / total_cnt)

    print('one:', stan_one, stan_one / total_cnt)
    print('zero:', stan_zero, stan_zero / total_cnt)
