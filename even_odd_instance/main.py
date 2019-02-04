def instance_generator():
    def helper():
        nonlocal cnt
        cnt += 1
        if cnt % 2 == 0:
            return 1
        else:
            return 0


    cnt = 0
    return helper


if __name__ == '__main__':
    g = instance_generator()
    for i in range(5):
        print(g())
