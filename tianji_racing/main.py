def race(qingwang, tianji):
    def cmp(qingwang, arr):
        result = 0
        for i in range(len(qingwang)):
            if qingwang[i] > arr[i]:
                result -= 1
            else:
                result += 1
        return result, arr


    arr = pen(tianji)
    final_score = 0
    result = None
    for option in arr:
        score, card = cmp(qingwang, option)
        if score > final_score:
            result = card
    return result


def pen(arr):
    def helper(rest, trace, result):
        if not rest:
            result.append(trace)
        for i in range(len(rest)):
            next = rest[:i] + rest[i+1:]
            helper(next, trace + [rest[i]], result)


    result = []
    helper(arr, [], result)
    return result


if __name__ == '__main__':
    q = [9, 4, 6]
    t = [8, 3, 5]
    print(race(q, t))
