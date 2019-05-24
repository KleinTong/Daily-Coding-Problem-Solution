from indexedMinPq import ImprovedIndexedMinPq as IndexedMinPq


def convert(s):
    def count_s(s):
        record = {}
        for c in s:
            if c in record:
                record[c] += 1
            else:
                record[c] = 1
        return record


    def init_indexedMaxPq(char_cnt_dict):
        imq = IndexedMinPq()
        for key, value in char_cnt_dict.items():
            imq.push(key, -value)
        return imq


    def get_char(imq, prev_item):
        if not imq.empty():
            item = imq.delMin()
            return item
        elif prev_item:
            imq.push(prev_item.key, prev_item.value)
            return None


    result = ''
    imq = init_indexedMaxPq(count_s(s))
    prev_item = None
    while not imq.empty() or prev_item:
        # imq.display()
        item = get_char(imq, prev_item)
        if not item:
            prev_item = None
            continue
        result += item.key
        item.value += 1
        if prev_item:
            imq.push(prev_item.key, prev_item.value)
        if item.value < 0:
            prev_item = item
        else:
            prev_item = None
    return result


if __name__ == '__main__':
    s = 'abababccbs'
    print(convert(s))
    s = 'aaabbc'
    print(convert(s))
    s = 'aaab'
    print(convert(s))
