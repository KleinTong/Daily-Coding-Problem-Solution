from queue import Queue


def reverse_by_delimiters(s, delimiters):
    def delimiters_maker():
        d_dict = {}
        for item in delimiters:
            if item[0] not in d_dict:
                d_dict[item[0]] = [item]
        return d_dict


    def is_delimiter(index):
        def helper(index, delim):
            length = len(delim)
            if index + length >= len(s):
                return False
            if s[index:index+length] == delim:
                return True


        for value in d_dict[s[index]]:
            if helper(index, value):
                return value
        return None


    buf = ''
    result = []
    d_dict = delimiters_maker()
    q = Queue()
    index = 0
    s_length = len(s)
    while True:
        if index >= s_length:
            break
        if s[index] in d_dict:
            flag = is_delimiter(index)
            if flag:
                result.append(buf)
                q.put(flag)
                buf = ''
                index += len(flag)
            else:
                buf += s[index]
                index += 1
        else:
            buf += s[index]
            index += 1
    if buf:
        result.append(buf)
    while result:
        print(result.pop(), end='')
        if not q.empty():
            print(q.get(), end='')


if __name__ == '__main__':
    delimiters = ['/abc/', '()', ':']
    s = 'hell/abc/x/world:here'
    reverse_by_delimiters(s, delimiters)
