def find_group(d):
    marked = {}
    group = {}
    group_index = 0
    for key, value in d.items():
        if key in marked:
            index = marked[key]
            for node in value:
                if node not in marked:
                    marked[node] = index
                    group[index].append(node)
        else:
            marked[key] = group_index
            group[group_index] = [key]
            for node in value:
                marked[node] = group_index
                group[group_index].append(node)
            group_index += 1
    return group


if __name__ == '__main__':
    d = {
         0: [1, 2],
         1: [0, 5],
         2: [0],
         3: [6],
         4: [],
         5: [1],
         6: [3]
    }
    print(find_group(d))
