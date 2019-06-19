class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def get_neighbors(x, y, matrix):
    neighbors = []
    if x > 0 and matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    if y > 0 and matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    if y < len(matrix) - 1 and matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    return neighbors


def dft(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))
    while s.size() > 0:
        v = s.pop()
        if not visited[v[1]][v[0]]:
            visited[v[1]][v[0]] = True
            for neighbor in get_neighbors(v[0], v[1], matrix):
                s.push(neighbor)
    return visited


def island_counter(matrix):
    # Create a visited Matrix
    visited = []
    for _ in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    # create a counter
    island_count = 0
    # Walk through each cell in the matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # if not been visited...
            if not visited[y][x]:
                # when we reach a 1 in the data set...
                if matrix[y][x] == 1:
                    # do a DFT and mark each as visited
                    visited = dft(x, y, matrix, visited)
                    # increment counter by 1
                    island_count += 1
                else:
                    visited[y][x] = True

    return island_count


def print_matrix(matrix):
    for row in matrix:
        print("".join([str(i) for i in row]))


islands = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]

# print(get_neighbors((1, 0), islands))
print(island_counter(islands))  # ===> 4
print("--------------")
islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))  # ===> 13
print("-------------------------------------")
print_matrix(islands)
