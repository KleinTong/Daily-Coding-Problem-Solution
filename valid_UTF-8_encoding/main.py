from math import ceil


def valid_utf_8(arr):
    def helper(d):
        b = bin(d)[2:]
        if len(b) % 8 != 0:
            b = (8 - (len(b) % 8)) * '0' + b
        bytes = 0
        if b[0] == '0':
            bytes = 1
        else:
            for c in b[:8]:
                if c == '0':
                    break
                else:
                    bytes += 1
        if bytes > 8:
            return False
        if len(b) // 8 != bytes:
            return False
        for i in range(1, bytes):
            if b[i*8: i*8+2] != '10':
                return False
        return True


    for item in arr:
        print(bin(item)[2:], helper(item))


if __name__ == '__main__':
    arr = [
            int('00111', 2),
            int('1000011111000000', 2),
            int('11110000100000001000000010000000', 2)
        ]
    valid_utf_8(arr)
