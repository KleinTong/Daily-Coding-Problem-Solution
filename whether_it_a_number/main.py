def check(s):
    decimal_point_flag = False
    negative_flag = False
    scientific_flag = False
    if s[0] == '-':
        negative_flag = True
    length = len(s)
    numbers = [str(i) for i in range(10)]
    for i, c in enumerate(s):
        if c == '.':
            if not decimal_point_flag:
                decimal_point_flag = True
            else:
                return False
        elif (c == 'e' or c == 'E'):
            if not scientific_flag:
                scientific_flag = True
            else:
                return False
        elif c == '-':
            if i != 0:
                return False
            if i == length - 1:
                return False
        elif c not in numbers:
            return False
    if s[length-1] == 'e':
        return False
    return True


if __name__ == '__main__':
    strings = ['10', '-10', '-', 'ac', '1e5', '1*1', '-1e5', '1e', '1111e1']
    for s in strings:
        print(s, 'True' if check(s) else 'False')
