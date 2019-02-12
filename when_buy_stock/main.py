def make_arr(arr):
    result = []
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        result.append(diff)
    return result


def shrink(arr):
    arr = make_arr(arr)
    new_arr = []
    pos_sum = 0
    pos_cnt = 0
    neg_sum = 0
    neg_cnt = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            if neg_cnt > 0:
                new_arr.append(neg_sum)
                neg_sum = 0
                neg_cnt = 0
            pos_sum += arr[i]
            pos_cnt += 1
        else:
            if pos_cnt > 0:
                new_arr.append(pos_sum)
                pos_sum = 0
                pos_cnt = 0
            neg_sum += arr[i]
            neg_cnt += 1
    if pos_cnt > 0:
        new_arr.append(pos_sum)
    if neg_cnt > 0:
        new_arr.append(neg_sum)
    if new_arr[0] < 0:
        new_arr = new_arr[1:]
    if new_arr[-1] < 0:
        new_arr = new_arr[:-1]
    return new_arr


def buy_stocks(arr, k):
    def continue_shrink(diff_arr):
        final_arr = []
        i = 0
        while True:
            if i >= len(diff_arr):
                break
            if i + 1 >= len(diff_arr) and i + 2 >= len(diff_arr):
                final_arr.append(diff_arr[i])
                break
            if diff_arr[i] + diff_arr[i+1] > 0 and \
                diff_arr[i+1] + diff_arr[i+2] > 0:
                result = diff_arr[i] + diff_arr[i+1] + diff_arr[i+2]
                diff_arr[i+2] = result
                i += 2
            else:
                final_arr.append(diff_arr[i])
                i += 2
                if i + 1 >= len(diff_arr):
                    final_arr.append(diff_arr[i])
                    break
        return final_arr

    
    arr = shrink(arr)
    print(arr)
    # cnt = 0
    # pos_arr = []
    # for item in arr:
    #     if item > 0:
    #         cnt += 1
    #         pos_arr.append(item)
    # print(pos_arr)
    if len(arr) // 2 + 1 <= k:
        pos_arr.sort(reverse=True)
        sum = 0
        for i in range(k):
            sum += pos_arr[i]
        return sum
    else:
        final_arr = continue_shrink(arr)
        print(final_arr)
        final_arr.sort(reverse=True)
        final_result = 0
        for num in final_arr[:k]:
            final_result += num
        return final_result
        

if __name__ == '__main__':
    arr = [0, 7, 1, 17, 2, 88, 32, 37, 1, 10, 11, 13]
    print(buy_stocks(arr, 2))
