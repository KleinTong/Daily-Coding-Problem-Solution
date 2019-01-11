import math
import datetime


def era(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(1, n + 1):
        if isPrime[i]:
            index = i * 2
            while index < n + 1:
                isPrime[index] = False
                index += i
    result = {i : True for i in range(len(isPrime)) if isPrime[i]}
    # result = [i for i in range(len(isPrime)) if isPrime[i]]
    return result


def two_prime_sums(n):
    if n % 2 == 1:
        raise ValueError()
    primes = era(n)
    for key in primes.keys():
        if (n - key) in primes:
            return (key, n - key)
    # length = len(primes)
    # for i in range(length):
    #     for j in range(i, length):
    #         if primes[i] + primes[j] == n:
    #             return (primes[i], primes[j])
    return (-1, -1)

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    # print(era(100))
    # print(era(3000))
    # print(era(9))
    for i in range(4, 10000, 2):
        print(i, two_prime_sums(i))
    end_time = datetime.datetime.now()
    print('run time is', end_time - start_time)
    # print(two_prime_sums(4))
    # print(two_prime_sums(40))
