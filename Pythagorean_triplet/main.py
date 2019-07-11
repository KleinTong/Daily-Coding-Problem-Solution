def triplet(arr):
    arr.sort()
    d = {}
    for n in arr:
        num = n**2
        d[num] = n
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (arr[i]**2 + arr[j]**2) in d:
                key = arr[i]**2 + arr[j]**2
                item = d[key]
                print('{}**2 + {}**2 = {}**2 = {}'.format(arr[i], arr[j], item, key))


if __name__ == '__main__':
    arr = [3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17, 20, 21, 24, 25, 28, 29, 33, 35, 36, 37, 39, 40, 41, 45, 48, 53, 55, 56, 60, 61, 63, 65, 72, 73, 77, 80, 84, 85, 89, 97]
    triplet(arr)
