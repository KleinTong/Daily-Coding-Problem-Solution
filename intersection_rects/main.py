def intersection(rect_1, rect_2):
    r_1_top_left = rect_1['top_left']
    r_1_width = rect_1['dimensions'][0]
    r_1_height = rect_1['dimensions'][1]
    r_1_bottom_right = (r_1_top_left[0] + r_1_width, r_1_top_left[1] + r_1_height)

    r_2_top_left = rect_2['top_left']
    r_2_width = rect_2['dimensions'][0]
    r_2_height = rect_2['dimensions'][1]
    r_2_bottom_right = (r_2_top_left[0] + r_2_width, r_2_top_left[1] + r_2_height)

    int_top_left = (max(r_1_top_left[0], r_2_top_left[0]), max(r_1_top_left[1], r_2_top_left[1]))
    int_bottom_right = (min(r_1_bottom_right[0], r_2_bottom_right[0]), min(r_1_bottom_right[1], r_2_bottom_right[1]))

    width = int_bottom_right[0] - int_top_left[0]
    height = int_bottom_right[1] - int_top_left[1]

    if width < 0 or height < 0:
        return 0
    else:
        return width * height


if __name__ == '__main__':
    rect_1 = {
        "top_left": (1, 4),
        "dimensions": (3, 3) # width, height
    }

    rect_2 = {
        "top_left": (3, 6),
        "dimensions": (4, 3) # width, height
    }

    print(intersection(rect_1, rect_2))
