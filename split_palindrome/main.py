def palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length-1-i]:
            return False
    return True


def split(s):
    def pre_processor():
        record = {}
        for key, c in enumerate(s):
            if c not in record:
                record[c] = [key]
            else:
                record[c].append(key)
        return record


    record = pre_processor()


    def helper(index, rest, trace):
        if not rest:
            return trace
        for i in record[rest[0]]:
            if i > index:
                word_length = i - index + 1
                if palindrome(rest[:word_length]):
                    use_it = helper(i+1, rest[word_length:], [rest[:word_length]])
                    # print('use_it', use_it)
                    not_use_it = helper(index + 1, rest[1:], [rest[0]])
                    # print('not_use_it', not_use_it)
                    if len(use_it) <= len(not_use_it):
                        return trace + use_it
                    else:
                        return trace + not_use_it
        return trace + helper(index + 1, rest[1:], [rest[0]])


    return helper(0, s, [])


if __name__ == '__main__':
    s = 'racecarannakayak'
    # s = 'abccaba'
    # print(split_to_palindrome(s))
    print(split(s))
