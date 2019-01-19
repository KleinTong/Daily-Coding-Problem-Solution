def main(s, characters):
    def find_max_min(d):
        min = 100
        max = -1
        for key, value in d.items():
            if value < min:
                min = value
            if value > max:
                max = value
        return min, max


    chosen = {}
    cnt = 0
    length = len(characters)
    ans_length = float('inf')
    left = -1
    right = -1
    for i, c in enumerate(s):
        if c in characters:
            if c not in chosen:
                chosen[c] = i
                cnt += 1
            else:
                chosen[c] = i
            if cnt == length:
                min, max = find_max_min(chosen)
                l = (max - min + 1)
                if ans_length > l:
                    ans_length = l
                    left = min
                    right = max
                # print(chosen)
                # print(min, max)
    # print(left, right)
    result = s[left:right+1]
    return result if result else None


if __name__ == '__main__':
    s = 'figaeheicijjjjjjaa'
    # s = 'ijh'
    characters = ['a', 'e', 'i']
    print(main(s, characters))
