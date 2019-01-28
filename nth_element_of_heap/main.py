def n_th(heap, k):
    pool = [1]
    cnt = 0
    heap_length = len(heap)
    while cnt != k:
        min_ele = float('inf')
        index = -1
        for i in pool:
            if min_ele > heap[i]:
                min_ele = heap[i]
                index = i
        pool.remove(index)
        left_index = 2 * index
        right_index = 2 * index + 1
        if left_index < heap_length:
            pool.append(left_index)
        if right_index < heap_length:
            pool.append(right_index)
        cnt += 1
    return min_ele


if __name__ == '__main__':
    heap = [None, 1, 2, 8, 4, 5, 12, 17, 9]
    print(n_th(heap, 6))
