def is_valid(filename):
    vertices = {}
    opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    def add_vertex(vertices, v):
        if v not in vertices:
            vertices[v] = {'N': set(), 'S': set(), 'W': set(), 'E': set()}


    def check_valid(v):
        item = vertices[v]
        if item['N'].intersection(item['S']):
            return False
        if item['E'].intersection(item['W']):
            return False
        return True


    try:
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                content = line.split()
                v1 = content[0]
                v2 = content[2]
                pos = content[1]
                add_vertex(vertices, v1)
                add_vertex(vertices, v2)
                if len(pos) > 2:
                    raise ValueError('wrong pos')
                for c in pos:
                    vertices[v2][c].add(v1)
                    for node in vertices[v1][c]:
                        vertices[v2][c].add(node)
                        vertices[node][opposite[c]].add(v2)
                    vertices[v1][opposite[c]].add(v2)
                    for node in vertices[v2][opposite[c]]:
                        vertices[v1][opposite[c]].add(node)
                        vertices[node][c].add(v1)
                # print(vertices)
                if not check_valid(v1) or not check_valid(v2):
                    return False
    except:
        pass

    return True


if __name__ == '__main__':
    print(is_valid('content.txt'))
