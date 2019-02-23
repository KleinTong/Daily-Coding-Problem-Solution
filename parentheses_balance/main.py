def parentheses_balance(s):
    def helper(rest, cnt):
        if not rest:
            if cnt != 0:
                return False
            else:
                return True
        for i in range(len(rest)):
            if rest[i] == '(':
                return helper(rest[1:], cnt + 1)
            elif rest[i] == ')':
                if cnt - 1 < 0:
                    return False
                else:
                    return helper(rest[1:], cnt - 1)
            elif rest[i] == '*':
                options = ['(', ')', ' ']
                result = False
                for option in options:
                    result = result or helper(option + rest[1:], cnt)
                return result
            else:
                return helper(rest[1:], cnt)


    return helper(s, 0)


if  __name__ == '__main__':
    s = '(()*'
    print(parentheses_balance(s))
    s = ')*('
    print(parentheses_balance(s))
    s = '((()****)))))'
    print(parentheses_balance(s))
