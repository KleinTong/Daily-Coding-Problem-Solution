def anagrams_indices(w, s):
    length = len(s)
    def helper(rest, i):
        if i >= length:
            return False
        if s[i] in rest:
            rest.remove(s[i])
            if not rest:
                return True
            return helper(rest, i+1)
        else:
            return False


    result = []
    w_arr = list(w)
    for i in range(length):
        word = w_arr.copy()
        if helper(word, i):
            result.append(i)
    return result


if __name__ == '__main__':
    s = 'abxaba'
    w = 'ab'
    print(anagrams_indices(w, s))
    s = 'xlimyximld'
    w = 'iml'
    print(anagrams_indices(w, s))
