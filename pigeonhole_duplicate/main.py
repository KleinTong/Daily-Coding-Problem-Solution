# if only one duplicate
def pigeonhole(arr, n):
    result = 0
    for i in range(1, n+1):
        result ^= i
    for num in arr:
        result ^= num
    return result


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 4]
    print(pigeonhole(a, 5))
