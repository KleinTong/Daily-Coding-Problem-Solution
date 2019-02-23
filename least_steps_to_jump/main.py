def least_steps(arr):
    def helper(pos, steps_cnt):
        if pos > len(arr):
            return float('inf')
        if pos == len(arr):
            return steps_cnt
        result = float('inf')
        for i in range(1, arr[pos]+1):
            result = min(result, helper(pos + i, steps_cnt + 1))
        return result


    return helper(0, 0)


if __name__ == '__main__':
    arr = [1, 3, 4, 2, 1, 1]
    print(least_steps(arr))
    arr = [1, 1, 1, 1, 1, 1]
    print(least_steps(arr))
