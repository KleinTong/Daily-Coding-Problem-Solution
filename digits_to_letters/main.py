def main(d, s):
    def helper(rest, result):
        if not rest:
            all_result.append(result)
            return
        if not rest[0] in d:
            raise ValueError()
        for item in d[rest[0]]:
            helper(rest[1:], result + item)


    all_result = []
    helper(s, '')
    return all_result


if __name__ == '__main__':
    d = {'2': ["a", "b", "c"], '3': ["d", "e", "f"]}
    print(main(d, '23'))
