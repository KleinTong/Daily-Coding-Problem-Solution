def cnt_islands(filename=None):
    def init_grid(filename):
        grid = []
        if filename:
            try:
                with open(filename, 'r') as f:
                    while True:
                        line = f.readline()
                        if not line:
                            break
                        content = line.split()
                        for i in range(len(content)):
                            content[i] = int(content[i])
                        grid.append(content)
            except:
                pass
        return grid


    def is_out_of_bounds(x, y, x_border, y_border):
        if x < 0 or x >= x_border:
            return True
        if y < 0 or y >= y_border:
            return True
        return False


    def explore(grid, x, y, index, x_border, y_border):
        if is_out_of_bounds(x, y, x_border, y_border):
            return
        if grid[x][y] == 0 or grid[x][y] != 1:
            return
        grid[x][y] = index
        explore(grid, x, y + 1, index, x_border, y_border)
        explore(grid, x, y - 1, index, x_border, y_border)
        explore(grid, x - 1, y, index, x_border, y_border)
        explore(grid, x + 1, y, index, x_border, y_border)
        return


    def display_grid(grid, x_border, y_border):
        for i in range(x_border):
            for j in range(y_border):
                print(grid[i][j], end=' ')
            print()


    grid = init_grid(filename)
    index = 1
    num = 0
    x_border = len(grid)
    y_border = len(grid[0])
    for i in range(x_border):
        for j in range(y_border):
            if grid[i][j] == 1:
                index += 1
                num += 1
            explore(grid, i, j, index, x_border, y_border)

    display_grid(grid, x_border, y_border)
    print('islands num is', num)
    return num


if __name__ == '__main__':
    cnt_islands('islands.txt')
