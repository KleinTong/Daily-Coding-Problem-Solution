def permution_palindrome(s):
    def permution(trace, rest):
        if not rest:
            return check_palindrome(trace)
        for index, c in enumerate(rest):
            if permution(trace + c, rest[:index] + rest[index+1:]):
                return True
        return False


    def check_palindrome(s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 -i]:
                return False
        return True


    return permution('', s)


if __name__ == '__main__':
    s = 'carrace'
    print(permution_palindrome(s))
    s = 'travel'
    print(permution_palindrome(s))
    s = 'a'
    print(permution_palindrome(s))
