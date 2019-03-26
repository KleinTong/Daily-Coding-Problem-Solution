from random import random


def markov(arr):
    def cook_data():
        data = {}
        for item in arr:
            begin = item[0]
            prob = item[1], item[2]
            if begin not in data:
                data[begin] = [prob]
            else:
                data[begin].append(prob)
        return data


    def machine(start, steps):
        data = cook_data()
        cnt = 0
        result = {}
        item = start
        while True:
            if cnt >= steps:
                break
            p = random()
            r = 0
            for prob in data[item]:
                r += prob[1]
                if r >= p:
                    if prob[0] not in result:
                        result[prob[0]] = 1
                    else:
                        result[prob[0]] += 1
                    item = prob[0]
                    cnt += 1
                    break
        return result


    return machine


if __name__ == '__main__':
    arr = [
      ('a', 'a', 0.9),
      ('a', 'b', 0.075),
      ('a', 'c', 0.025),
      ('b', 'a', 0.15),
      ('b', 'b', 0.8),
      ('b', 'c', 0.05),
      ('c', 'a', 0.25),
      ('c', 'b', 0.25),
      ('c', 'c', 0.5)
    ]
    machine = markov(arr)
    for _ in range(10):
        print(machine('a', 5000))
