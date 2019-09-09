def reduce(arr, fn, initial):
    result = initial

    for item in arr:
        result = fn(result, item)

    return result


def add(a, b):
    return a + b


if __name__ == "__main__":
    print(reduce([1, 2, 3], add, 0))