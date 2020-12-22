import enchant

wordcheck = enchant.Dict('en_US')

grid = [
     ['p', 's', 'a', 'a'],
    ['a', 'p', 'w', 'i'],
    ['p', 'o', 'e', 's'],
    ['a', 't', 't', 'p']
]


class Node:
    def __init__(self, data, pos):
        self.data = data
        self.children = []
        self.y = pos[0]
        self.x = pos[1]

    def add_child(self, child):
        self.children.append(child)
        child.children.append(self)

    def print_children(self, isData=True):
        if isData:
            return [i.data for i in self.children]
        else:
            return [i for i in self.children]

    def has_pos(self, pos):
        if self.x == pos[1] and self.y == pos[0]:
            return True
        return False


class Graph:
    def __init__(self):
        self.nodes = []
        for y in range(len(grid)):
            for x in range(len(grid)):
                self.nodes.append(Node(grid[y][x], [y, x]))
        for i in self.nodes:
            for j in self.get_surrounding_nodes(i):
                j.add_child(i)

    def has_key(self, key):
        if key in self.nodes:
            return True
        return False

    #returns surrounding letters of certain position and converts them to nodes
    def get_surrounding_nodes(self, node):
        if node.y == 0 and node.x == 0:
            surrounding = [[1, 0], [1, 1], [0, 1]]
        elif node.y == 0 and node.x == len(grid)-1:
            surrounding = [[1, 0], [1, -1], [0, -1]]
        elif node.y == len(grid)-1 and node.x == 0:
            surrounding = [[-1, 0], [-1, 1], [0, 1]]
        elif node.y == len(grid)-1 and node.x == len(grid)-1:
            surrounding = [[-1, 0], [-1, -1], [0, -1]]
       #EDGES

        elif node.y == len(grid)-1:
            surrounding = [[-1, 0], [0, 1], [0, -1], [-1, 1], [-1,-1]]
        elif node.x == len(grid)-1:
            surrounding = [[1, 0], [-1, 0], [0, -1], [1, -1], [-1,-1]]
        elif node.y == 0:
            surrounding = [[1, 0], [0, 1], [0, -1], [1, 1], [1,-1]]
        elif node.x == 0:
            surrounding = [[1, 0], [-1, 0], [0, 1], [1, 1], [-1, 1]]

        else:
            surrounding = [[1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        final = list()

        for i in range(len(surrounding)):
            y = surrounding[i][0]
            x = surrounding[i][1]
            for node in self.nodes:
                if node.has_pos([y, x]):
                    final.append(node)
        return final


    def find_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.nodes:
            return []
        paths = []
        for node in start.children:
            if node not in path:
                newpath = self.find_paths(node, end, path)
                for p in newpath:
                    paths.append(p)
        return paths

    def all_combinations(self):
        paths = []
        for i in range(len(self.nodes)):
            for j in range(i, len(self.nodes)):
                paths.append(self.find_paths(self.nodes[i], self.nodes[j]))
        return paths


boggle = Graph()

for i in boggle.find_paths(boggle.nodes[0], boggle.nodes[1]):
    for j in i:
        print(''.join(j.data))
