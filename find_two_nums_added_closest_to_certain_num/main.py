def find_two(arr_1, arr_2, target):
    arr_1.sort()
    arr_2.sort()
    print(arr_1)
    print(arr_2)
    def helper(i, left, right):
        if left >= right:
            return left
        mid = (left + right) // 2
        if arr_1[i] + arr_2[mid] > target:
            result = helper(i, left, mid)
            if abs(target - arr_1[i] - arr_2[result]) < abs(target - arr_1[i] - arr_2[mid]):
                return result
            else:
                return mid
        elif arr_1[i] + arr_2[mid] < target:
            result = helper(i, mid + 1, right)
            if abs(target - arr_1[i] - arr_2[result]) < abs(target - arr_1[i] - arr_2[mid]):
                return result
            else:
                return mid
        else:
            return mid


    result = float('inf')
    index = 0
    for i in range(len(arr_1)):
        item = helper(i, 0, len(arr_2) - 1)
        if abs(arr_1[i] + arr_2[item] - target) < result:
            index = i, item
            result = abs(arr_1[i] + arr_2[item] - target)
    return arr_1[index[0]], arr_2[index[1]]


if __name__ == '__main__':
    arr_1 = [-1, 3, 8, 2, 4, 5]
    arr_2 = [4, 1, 2, 10, 5, 20]
    print(find_two(arr_1, arr_2, 24))
