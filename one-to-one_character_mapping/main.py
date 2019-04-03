def check_map(s1, s2):
    def calculate_letters(s):
        record = {}
        cnt = 0
        for c in s:
            if c not in record:
                record[c] = True
                cnt += 1
        return cnt


    if calculate_letters(s1) != calculate_letters(s2):
        return False
    else:
        return True


if __name__ == '__main__':
    s1 = 'abc'
    s2 = 'bcd'
    print(check_map(s1, s2))
    s1 = 'foo'
    s2 = 'c-1'
    print(check_map(s1, s2))
    s1 = 'f00'
    s2 = 'opp'
    print(check_map(s1, s2))
