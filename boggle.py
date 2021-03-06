import enchant
import time

wordcheck = enchant.Dict('en_US')

grid = [
     ['f', 's', 'b', 'e'],
    ['d', 'l', 'o', 'b'],
    ['a', 'i', 'e', 'o'],
    ['y', 'l', 'm', 'o']
]


class Node:
    def __init__(self, data, pos):
        self.data = data
        self.children = []
        self.y = pos[0]
        self.x = pos[1]

    def add_child(self, child):
        self.children.append(child)

    def print_children(self):
        return [i.data for i in self.children]

    def has_pos(self, y, x):
        if self.x == x and self.y == y:
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
            surrounding = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        final = list()

        for i in surrounding:
            absolute_x = i[1] + node.x
            absolute_y = i[0] + node.y
            for j in self.nodes:
                if j.has_pos(absolute_y, absolute_x):
                    final.append(j)
                    break
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
                paths = paths + self.find_paths(self.nodes[i], self.nodes[j])
        return paths

    def print_nodes(self):
        for i in self.nodes:
            print(i.data, i.print_children())

time1 = time.time()
boggle = Graph()


node1 = boggle.nodes[4]
node2 = boggle.nodes[12]

wordlist = set()

for i in boggle.all_combinations():
    word = ''.join([j.data for j in i])
    if len(word) > 2 and wordcheck.check(word):
        wordlist.add(word)


print(wordlist)
print(time.time() - time1)
