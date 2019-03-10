def gray_code(n):
    result = []
    def helper(rest, trace):
        if rest == 0:
            result.append(trace)
            return
        helper(rest-1, trace + '0')
        helper(rest-1, trace + '1')


    helper(n, '')
    return result


if __name__ == '__main__':
    result = gray_code(5)
    print(len(result))
    print(result)
