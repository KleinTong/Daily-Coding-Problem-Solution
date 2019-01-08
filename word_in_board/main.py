def is_word_in_board(board, word):
    height = len(board)
    width = len(board[0])
    character_dict = {}

    def init_dict(character_dict):
        for i in range(height):
            for j in range(width):
                c = board[i][j]
                if c in character_dict:
                    character_dict[c].append((i, j))
                else:
                    character_dict[c] = [(i, j)]


    def init_marked():
        marked = [[False for _ in range(width)] for _ in range(height)]
        return marked


    def is_out_of_bounds(i, j):
        if i < 0 or i >= height:
            return True
        if j < 0 or j >= width:
            return True
        return False


    def helper(i, j, rest, marked):
        if is_out_of_bounds(i, j):
            return False
        if marked[i][j]:
            return False
        marked[i][j] = True
        if board[i][j] == rest[0]:
            if len(rest) == 1:
                return True
            else:
                one = helper(i + 1, j, rest[1:], marked)
                two = helper(i - 1, j, rest[1:], marked)
                three = helper(i, j + 1, rest[1:], marked)
                four = helper(i, j - 1, rest[1:], marked)
                if one or two or three or four:
                    return True
                else:
                    return False
        else:
            return False


    init_dict(character_dict)
    for item in character_dict[word[0]]:
        marked = init_marked()
        result = helper(item[0], item[1], word, marked)
        if result:
            return True

    return False


if __name__ == '__main__':
    board = [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
    ]
    print(is_word_in_board(board, 'ABCCED'))
    print(is_word_in_board(board, 'ABCB'))
    print(is_word_in_board(board, 'SEE'))
    print(is_word_in_board(board, 'CCEDAS'))
