from operator import add, sub, truediv, mul


def polish(s):
    operator_dict = {'+': add, '-': sub, '/':truediv, '*': mul}


    def helper(rest):
        for i in range(len(rest)):
            if rest[i] in operator_dict:
                try:
                    result = operator_dict[rest[i]](rest[i-1], rest[i-2])
                    rest = rest[:i-2] + [result] + rest[i+1:]
                except:
                    print('wrong input')
                    exit()
                return helper(rest)
        if len(rest) == 1:
            return rest[0]
        else:
            print('wrong input')
            exit()


    return helper(s)


if __name__ == '__main__':
    s = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
    print(polish(s))
    s = [1, 1, 1, '+']
    print(polish(s))
