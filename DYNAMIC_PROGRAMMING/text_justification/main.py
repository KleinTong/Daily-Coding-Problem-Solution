def justify(s, width):
    def helper(i, trace):
        if i == length:
            return 0, trace
        final_result = float('inf')
        final_trace = []
        i_trace = trace + [i]
        for j in range(i + 1, length + 1):
            line_1_badness = badness(i, j)
            if line_1_badness == float('inf'):
                continue
            rest_line_badness, j_trace = helper(j, i_trace)
            result = line_1_badness + rest_line_badness
            if result < final_result:
                final_result = result
                final_trace = j_trace
        return final_result, final_trace


    def used_width_cnt(i, j):
        length = 0
        words = s_arr[i:j]
        for word in words:
            length += len(word)
        if len(words) == 1:
            return length
        else:
            length += (len(words) - 1)
        return length


    def badness(i, j):
        used_width = used_width_cnt(i, j)
        if used_width > width:
            return float('inf')
        return (width - used_width) ** 3


    def print_line(trace):
        length = len(trace)
        for i in range(length):
            if i + 1 < length:
                for word in s_arr[trace[i]:trace[i+1]]:
                    print(word, end=' ')
                print()
            else:
                for word in s_arr[trace[i]:]:
                    print(word, end=' ')
                print()


    s_arr = s.split()
    length = len(s_arr)
    result, trace = helper(0, [])
    print(trace)
    print(result)
    print_line(trace)


def compute_badness(sentences_arr, max_width):
    result = 0
    for sentence in sentences_arr:
        words = sentence.split()
        words_used_space = 0
        for word in words:
            words_used_space += len(word)
        words_used_space += len(words) - 1
        result += (max_width - words_used_space) ** 3
    return result


if __name__ == '__main__':
    s = 'origBoard and aiPlayer is fed to the algorithm.'
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["What","must","be","acknowledgment","shall","be"]
    words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
    s = ' '.join(words)
    print(s)
    max_width = 20
    print('a' * 20)
    justify(s, max_width)
    greedy_words = [
      "Science  is  what we",
      "understand      well",
      "enough to explain to",
      "a  computer.  Art is",
      "everything  else  we",
      "do                  "
    ]
    print(compute_badness(greedy_words, 20))
