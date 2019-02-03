def make_palindrome(k, s):
    def check_palindrome(word):
        length = len(word)
        for i in range(0, length // 2 + 1):
            if word[i] != word[length - 1 -i]:
                return False
        return True


    def helper(times, rest):
        if check_palindrome(rest):
            return rest
        if not rest:
            return ''
        if times == 0:
            return ''
        length = len(rest)
        for i in range(length):
            result = helper(times - 1, rest[0:i] + rest[i+1:])
            if result:
                return result
        return ''


    return helper(k, s)


if __name__ == '__main__':
    k = 2
    s = 'waterrfetawx'
    print(make_palindrome(k, s))
    s = 'abzccoba'
    print(make_palindrome(k, s))
