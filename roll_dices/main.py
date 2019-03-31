from random import randint, seed
from datetime import datetime


def roll_maker(pattern):
    last_roll = ''


    def roll():
        nonlocal last_roll
        seed(datetime.now())
        cnt = 0
        while True:
            cnt += 1
            i = str(randint(1, 7))
            if last_roll + i == pattern:
                return cnt
            else:
                last_roll = i


    return roll


if __name__ == '__main__':
    roll_1 = roll_maker('55')
    roll_2 = roll_maker('56')
    roll_3 = roll_maker('12')

    for _ in range(10):
        result_1 = 0
        result_2 = 0
        result_3 = 0
        for _ in range(10000):
            r_1 = roll_1()
            r_2 = roll_2()
            r_3 = roll_3()
            bigOne = max(r_1, r_2, r_3)
            if r_1 == bigOne:
                result_1 += 1
            elif r_2 == bigOne:
                result_2 += 1
            elif r_3 == bigOne:
                result_3 += 1
        print('1: {}'.format(result_1))
        print('2: {}'.format(result_2))
        print('3: {}'.format(result_3))
        print()
