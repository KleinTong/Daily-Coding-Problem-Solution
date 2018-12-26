def remove_p(s):
    left_p = []
    right_p = []
    num = 0
    for c in s:
        if c == '(':
            left_p.append('(')
        elif c == ')':
            if not left_p:
                num += 1
            else:
                left_p.pop()
        else:
            raise ValueError('wrong character')
    num += len(left_p)
    return num


if __name__ == '__main__':
    s = '()())()'
    print(remove_p(s))
    s = ')('
    print(remove_p(s))
