from queue import Queue


def interleave(s):
    q = Queue()
    cnt = 0
    for _ in range(len(s) - 1):
        q.put(s.pop())
    while True:
        if q.empty():
            break
        s.append(q.get())
        time = q.qsize()
        for _ in range(time):
            s.append(q.get())
        for _ in range(time):
            q.put(s.pop())
    return s


if __name__ == '__main__':
    s = [i for i in range(1, 6)]
    print(interleave(s))
    s = [i for i in range(1, 5)]
    print(interleave(s))
