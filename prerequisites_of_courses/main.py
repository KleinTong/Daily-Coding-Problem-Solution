def prerequisites(courses_list):
    def helper(lesson, marked, lessons_took):
        if lesson in marked:
            return True
        marked[lesson] = True
        try:
            courses = courses_list[lesson]
        except:
            # raise ValueError('wrong course')
            return None
        for course in courses:
            x = helper(course, marked, lessons_took)
            if not x:
                return None
        lessons_took.append(lesson)
        return True


    lessons_took = []
    marked = {}
    for key in courses_list.keys():
        x = helper(key, marked, lessons_took)
        if not x:
            return None
    return lessons_took


if __name__ == '__main__':
    courses_list = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
    # courses_list = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': [], 'CSC105': ['CSC999']}
    print(prerequisites(courses_list))
