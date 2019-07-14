def get_building_setting_sun_backward(arr):
    max = -float('inf')
    results = []
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max:
            max = arr[i]
            results.append(arr[i])
    return results


def get_building_setting_sun_forward(arr):
    partly_high_building = []
    for i in arr:
        term = [i]
        for build in partly_high_building:
            if build > i:
                term.append(build)
        partly_high_building = term

    return partly_high_building



if __name__ == '__main__':
    arr = [3, 7, 8, 3, 6, 1]
    print(get_building_setting_sun_backward(arr))
    print(get_building_setting_sun_forward(arr))
