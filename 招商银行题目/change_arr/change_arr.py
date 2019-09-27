def longest_increasing_path(arr):
    def helper(index, max, record, length):
        final_length = -float('inf')
        final_result = []
        no_bigger = True
        for i in range(index, len(arr)):
            if arr[i] > max:
                no_bigger = False
                part_length, part_result = helper(i, arr[i], record + [arr[i]], length + 1)
                if part_length > final_length:
                    final_length = part_length
                    final_result = part_result
        if no_bigger:
            return length, record
        return final_length, final_result

    
    return helper(0, -float('inf'), [], 0)


if __name__ == '__main__':
    arr = [1, 2, 12, 5, 11]
    print(longest_increasing_path(arr))
    arr = [3, 10, 2, 1, 20]
    print(longest_increasing_path(arr))
