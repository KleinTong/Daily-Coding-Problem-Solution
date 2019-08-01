def calculate_degree(s):
    hour, minute = s.split(':')
    hour = int(hour)
    minute = int(minute)
    hour_deg = hour * 30
    # hour_deg = hour / 12 * 360
    minute_deg = minute * 6
    # minute_deg = minute / 60 *  360

    if hour_deg < minute_deg:
        temp = hour_deg
        hour_deg = minute_deg
        minute_deg = temp

    result = (hour_deg - minute_deg) + (minute / 2)
    return  result % 180 if result > 180 else result


def print_zero_degree():
    for i in range(0, 12):
        for j in range(0, 60):
            s = str(i) + ':' + str(j)
            result = calculate_degree(s)
            print(i, j, result)
            if result == 0:
                print(s)


if __name__ == '__main__':
    print(calculate_degree('11:10'))
    print(calculate_degree('00:00'))
    print(calculate_degree('06:00'))
    print_zero_degree()
