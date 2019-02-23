def find_two(arr):
    repo_dict = {}
    for item in arr:
        if item not in repo_dict:
            repo_dict[item] = 1
        else:
            repo_dict.pop(item)
    return list(repo_dict.keys())


if __name__ == '__main__':
    arr = [2, 4, 6, 8, 10, 2, 6, 10]
    print(find_two(arr))
