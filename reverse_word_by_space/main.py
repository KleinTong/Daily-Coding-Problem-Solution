def reverse_word(s):
    def helper(rest):
        if not rest:
            return
        helper(rest[1:])
        print(rest[0], end=' ')


    rest = s.split()
    helper(rest)
    print()


if __name__ == '__main__':
    s = 'hello world easy bro'
    reverse_word(s)
