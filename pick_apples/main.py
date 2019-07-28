def pick_apples(arr):
    marked_item = [None, None]
    max_item = [None, None]
    max_cnt = 0
    current_cnt = 0
    prev_item = None
    prev_item_cnt = 0
    for item in arr:
        if item not in marked_item:
            marked_item = [item, prev_item]
            current_cnt = prev_item_cnt + 1
        else:
            current_cnt += 1

        if item == prev_item:
            prev_item_cnt += 1
        else:
            prev_item = item
            prev_item_cnt = 1

        if current_cnt > max_cnt:
            max_cnt = current_cnt
            max_item = marked_item
        print(item, max_cnt, marked_item)
    return max_cnt, max_item


if __name__ == '__main__':
    arr = [2, 1, 2, 1, 2, 2, 3, 3, 1, 3, 1, 5]
    print(pick_apples(arr))
