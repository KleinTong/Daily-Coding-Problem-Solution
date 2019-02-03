def cover(intervals):
    def get_num_cnt(num_dict):
        for interval in intervals:
            if interval[0] not in num_dict:
                num_dict[interval[0]] = 1
            else:
                num_dict[interval[0]] += 1
            if interval[1] not in num_dict:
                num_dict[interval[1]] = 1
            else:
                num_dict[interval[1]] += 1


    def get_partener(partener_dict):
        for interval in intervals:
            if interval[0] not in partener_dict:
                partener_dict[interval[0]] = [interval[1]]
            else:
                partener_dict[interval[0]].append(interval[1])
            if interval[1] not in partener_dict:
                partener_dict[interval[1]] = [interval[0]]
            else:
                partener_dict[interval[1]].append(interval[0])


    num_dict = {}
    partener_dict = {}
    result = []
    get_num_cnt(num_dict)
    get_partener(partener_dict)
    while True:
        max_key = max(num_dict, key=num_dict.get)
        if num_dict[max_key] == 0:
            break
        result.append(max_key)
        num_dict[max_key] = 0
        for item in partener_dict[max_key]:
            num_dict[item] -= 1
    return result


if __name__ == '__main__':
    intervals = [[0, 3], [2, 6], [3, 4], [6, 9], [4, 10], [4, 7]]
    print(cover(intervals))
