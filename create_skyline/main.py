def create_skyline(arr):
    def worker(arr):
        refined_arr = []
        arr_length = len(arr)
        current_pos = 0
        current_item = arr[0]
        inf_flag = False
        for key, item in enumerate(arr):
            if key == 0:
                continue
            # if item == -float('inf'):
            #     if not inf_flag:
            #         refined_arr.append((current_pos, key - 1, current_item))
            #         inf_flag = True
            #     continue
            # if inf_flag:
            #     current_pos = key
            #     current_item = item
            #     inf_flag = False
            #     continue
            if current_item != item:
                refined_arr.append((current_pos, key - 1, current_item))
                current_pos = key
                current_item = item
            if key == arr_length - 1:
                refined_arr.append((current_pos, key, current_item))

        return refined_arr


    skyline = []
    length = 0
    for item in arr:
        start_pos = item[0]
        end_pos = item[1]
        building_height = item[2]
        if end_pos > length - 1:
            skyline += [0 for _ in range(end_pos - length + 1)]
            length = len(skyline)
        for i in range(start_pos, end_pos + 1):
            if skyline[i] < building_height:
                skyline[i] = building_height

    print(skyline)
    return worker(skyline)


if __name__ == '__main__':
    arr = [(0, 15, 3), (4, 11, 5), (19, 23, 4)]
    print(create_skyline(arr))
