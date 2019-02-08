from random import randint


def coins_flip(n):
    def max_counter(arr):
        max = -float('inf')
        cnt = 0
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
                cnt = 1
            elif arr[i] == max:
                cnt += 1
        # print('Max Num is', max)
        return cnt


    if n < 0:
        raise ValueError()
    coins = [0 for i in range(n)]
    for i in range(n):
        cnt = 0
        while True:
            coin = randint(0, 1)
            cnt += 1
            if coin == 1:
                break
        coins[i] = cnt
    max_cnt = max_counter(coins)
    # print(max_cnt)
    # print(coins)
    # print(result)
    if max_cnt != 1:
        result = max(coins)
        result += coins_flip(max_cnt)
        return result
    else:
        coins.remove(max(coins))
        part = max(coins)
        return part
    # return result


if __name__ == '__main__':
    print(coins_flip(100))
