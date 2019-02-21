coins = [1, 5, 10, 25]


def make_coins(ammount):
    # return mininum number of coins
    def helper(rest, trace):
        if rest == 0:
            return 0, trace
        elif rest < 0:
            return float('inf'), None
        if rest in memo:
            return memo[rest], traces[rest]
        result = float('inf')
        result_trace = None
        chosen_coin = -1
        for i in coins:
            option, opt_trace = helper(rest - i, [])
            if option < result:
                chosen_coin = i
                result = option
                result_trace = opt_trace
        memo[rest] = result + 1
        traces[rest] = result_trace + [chosen_coin]
        return memo[rest], traces[rest]


    memo = {}
    traces = {}
    result, trace = helper(ammount, [])
    # print(memo)
    # print(traces)
    return result, trace


if __name__ == '__main__':
    print(make_coins(100))
    print(make_coins(5))
    print(make_coins(7))
    print(make_coins(16))
    print(make_coins(27))
