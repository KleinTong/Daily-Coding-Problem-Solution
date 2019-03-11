from random import random


def generator(nums, probs):
    def worker():
        r = random()
        for i, n in enumerate(probs):
            r -= n
            if r <= 0:
                return nums[i]


    return worker


def test(worker, n):
    record = {}
    for _ in range(n):
        num = worker()
        if num not in record:
            record[num] = 1
        else:
            record[num] += 1
    return record


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    probs = [0.1, 0.5, 0.2, 0.2]
    worker = generator(nums, probs)
    print(test(worker, 200000))
