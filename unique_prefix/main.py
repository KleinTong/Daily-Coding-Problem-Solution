class WordTree:
    def __init__(self):
        self.child = {}


    def insert(self, word):
        def helper(rest, pos):
            print(pos)
            if not rest:
                if 'empty' not in pos:
                    pos['empty'] = 1
                else:
                    pos['empty'] += 1
            elif rest[0] not in pos:
                if not rest[1:]:
                    pos[rest[0]] = {'empty': 1}
                else:
                    pos[rest[0]] = rest[1:]
            else:
                if len(rest[0]) == 1:
                    pos[rest[0]] = self.merge_two_words(pos[rest[0]], rest[1:])
                else:
                    helper(rest[1:], pos[rest[0]])


        helper(word, self.child)


    def merge_two_words(self, a_word, b_word):
        i = 0
        j = 0
        result = {}
        item = result
        while True:
            if i >= len(a_word) or j >= len(b_word):
                break
            if a_word[i] != b_word[j]:
                item[a_word[i]] = a_word[i+1:]
                item[b_word[j]] = b_word[j+1:]
                break
            else:
                item[a_word[i]] = {}
                item = item[a_word[i]]
                i += 1
                j += 1
        return result


    def iterate_prefix(self):
        def helper(node, trace):
            if not isinstance(node, dict):
                print(trace)
                return
            else:
                for key in node.keys():
                    if key == 'empty':
                        print(trace)
                    else:
                        helper(node[key], trace+key)


        helper(self.child, '')


def unique_prefix(arr):
    word_tree = WordTree()

    for word in arr:
        word_tree.insert(word)

    word_tree.iterate_prefix()


if __name__ == '__main__':
    arr = ['z', 'dog', 'ca', 'cat', 'apple', 'apricot', 'fish', 'insert', 'happy', 'engine', 'english']
    unique_prefix(arr)
