def first_recurring(s):
    record = {}
    for c in s:
        if c not in record:
            record[c] = True
        else:
            return c
    return None


if __name__  == '__main__':
    s = 'acbbac'
    print(first_recurring(s))
