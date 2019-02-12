def maximum_subarray(arr, k):
    def make_arr(arr):
        result = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            result.append(diff)
        return result


    def find_maximum(diff_arr, left, right):
        if left >= right:
            return (left, right, diff_arr[left])
        mid = (left + right) // 2
        left_result = left_max_start, left_max_end, left_max_value = find_maximum(diff_arr, left, mid)
        right_result = right_max_start, right_max_end, right_max_value = find_maximum(diff_arr, mid+1, right)
        crossing_result = crossing_start, crossing_end, crossing_value = find_crossing_maximum(diff_arr, left, right)

        if left_max_value >= right_max_value and left_max_value >= crossing_value:
            return left_result

        elif right_max_value >= left_max_value and right_max_value >= crossing_value:
            return right_result

        else:
            return crossing_result


    def find_crossing_maximum(diff_arr, left, right):
        mid = (left + right) // 2
        left_sum = -float('inf')
        left_index = -1
        sum = 0
        for i in range(mid, left - 1, -1):
            sum += diff_arr[i]
            if sum > left_sum:
                left_sum = sum
                left_index = i

        right_sum = -float('inf')
        right_index = -1
        sum = 0
        for j in range(mid + 1, right + 1):
            sum += diff_arr[j]
            if sum > right_sum:
                right_sum = sum
                right_index = j
        return left_index, right_index, left_sum + right_sum


    diff_arr = make_arr(arr)
    return find_maximum(diff_arr, 0, len(diff_arr) - 1)[2]


if __name__ == '__main__':
    arr = [5, 2, 4, 3, 10]
    print(maximum_subarray(arr, 3))
