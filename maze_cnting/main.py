def maze_cnt(filename):
    def is_outbound(i, j, size):
        if i < 0 or i >= size:
            return True
        if j < 0 or j >= size:
            return True
        return False


    def helper(maze, i, j, marked, final_pos, size):
        if is_outbound(i, j, size):
            return False
        if marked[i][j]:
            return False
        if maze[i][j] == 'X':
            return False
        marked[i][j] = True
        if (i, j) == final_pos:
            return True
        return helper(maze, i+1, j, marked, final_pos, size) or \
            helper(maze, i-1, j, marked, final_pos, size) or \
            helper(maze, i, j+1, marked, final_pos, size) or \
            helper(maze, i, j-1, marked, final_pos, size)


    with open(filename, 'r') as f:
        maze_number = int(f.readline())
        final_result = ''
        for _ in range(maze_number):
            maze = []
            maze_size = int(f.readline())
            in_pos = f.readline().split()
            in_pos = int(in_pos[0]) - 1, int(in_pos[1]) - 1
            out_pos = f.readline().split()
            out_pos = int(out_pos[0]) - 1, int(out_pos[1]) - 1
            for _ in range(maze_size):
                maze.append(f.readline())
            marked = [[False for _ in range(maze_size)] for _ in range(maze_size)]
            result = helper(maze, in_pos[0], in_pos[1], marked, out_pos, maze_size)
            if result:
                final_result += '1'
            else:
                final_result += '0'
        return final_result


if __name__ == '__main__':
    final_result = maze_cnt('in.txt')
    print(final_result)
