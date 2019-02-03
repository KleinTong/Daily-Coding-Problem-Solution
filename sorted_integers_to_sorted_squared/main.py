def worker(arr):
    def find_zero(arr, left, right):
        if left >= right:
            if arr[left] != 0:
                return -1
        mid = (left + right) // 2
        if arr[mid] > 0:
            return find_zero(arr, left, mid)
        elif arr[mid] < 0:
            return find_zero(arr, mid, right)
        else:
            return mid


    def slice_arr(arr):
        def helper(left, right):
            if left >= right:
                return -1, -1
            l_num = arr[left]
            r_num = arr[right]
            if l_num * r_num > 0:
                if l_num < 0:
                    return right, -1
                else:
                    return -1, left
            if l_num * r_num <= 0:
                l_index = -1
                r_index = -1
                if l_num == 0 and r_num == 0:
                    return -1, -1
                if l_num == 0:
                    r_index = right
                if r_num == 0:
                    l_index = left
                mid = (left + right) // 2
                l_neg_index, l_pos_index = helper(left, mid)
                r_neg_index, r_pos_index = helper(mid+1, right)
                l_index = max(l_neg_index, r_neg_index, l_index)
                pool = []
                if l_pos_index >= 0:
                    pool.append(l_pos_index)
                if r_pos_index >= 0:
                    pool.append(r_pos_index)
                if r_index >= 0:
                    pool.append(r_index)
                pool.sort()
                if pool:
                    r_index = pool[0]
                return l_index, r_index


        return helper(0, len(arr) - 1)


    def merge(left, right):
        i = left
        j = right
        if i == -1:
            zero_num = right
        else:
            zero_num = right - left - 1
        # m = left + 1
        result = []
        print(zero_num)
        while zero_num > 0:
            result.append(0)
            zero_num -= 1
        while True:
            if i < 0:
                while j < len(arr):
                    result.append(arr[j] ** 2)
                    j += 1
                break
            if j >= len(arr):
                while i >= 0:
                    result.append(arr[i] ** 2)
                    i -= 1
                break
            if (arr[i] ** 2) <= (arr[j] ** 2):
                result.append(arr[i] ** 2)
                i -= 1
            else:
                result.append(arr[j] ** 2)
                j += 1
        return result


    # zero_index = find_zero(arr, 0, len(arr) - 1)
    # if zero_index == -1:
    #     return None
    left_index, right_index = slice_arr(arr)
    print(left_index, right_index)
    return merge(left_index, right_index)


if __name__ == '__main__':
    arr = [-1, 0, 1, 2, 3]
    arr = [-12, -1, 0, 0, 0, 2]
    print(worker(arr))
