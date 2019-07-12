def regular_num(N):
    def helper(i):
        if i > N:
            return
        if i not in marked:
            marked[i] = True
            results.append(i)
            helper(i * 2)
            helper(i * 3)
            helper(i * 5)

    results = []
    marked = {}
    helper(2)
    results.sort()
    return results


if __name__ == '__main__':
    print(regular_num(100))
