class SparceArr:
    def __init__(self, arr, size):
        self.cnt = size
        self.not_zero_pool = {}
        for index, value in enumerate(arr):
            if value != 0:
                self.not_zero_pool[index] = value


    def set(self, i, val):
        if i < 0 or i >= self.cnt:
            raise ValueError()
        self.not_zero_pool[i] = val


    def get(self, i):
        if i < 0 or i >= self.cnt:
            raise ValueError()
        if i not in self.not_zero_pool:
            return 0
        else:
            return self.not_zero_pool[i]


if __name__ == '__main__':
    arr = [0 for _ in range(1000)]
    arr[100] = 1
    arr[10] = 10
    s = SparceArr(arr, 1000)
    print(s.not_zero_pool)
