from math import sqrt


def squared_nums_sum(n):
    record = {}
    def helper(num):
        if num in record:
            return record[num]
        if num == 0:
            return 0, []
        if num < 0:
            return float('inf'), []
        final_result = float('inf')
        final_choice = -1
        rest = []
        for i in range(1, int(sqrt(num)) + 1):
            result, choice = helper(num - i ** 2)
            if result < final_result:
                final_result = result
                final_choice = i
                rest = choice
        record[num] = final_result + 1, [final_choice] + rest
        return record[num]


    return helper(n)


if __name__ == '__main__':
    for i in range(100):
        print(i, squared_nums_sum(i))
    # print(squared_nums_sum(13))
    # print(squared_nums_sum(27))
