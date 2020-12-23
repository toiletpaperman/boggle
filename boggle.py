import enchant
import time
import concurrent.futures
import multiprocessing

wordcheck = enchant.Dict('en_US')

grid = [
     ['o', 'o', 's', 'f'],
    ['o', 's', 'l', 'b'],
    ['n', 'l', 'o', 't'],
    ['l', 'qu', 'i', 'r']
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
        processes = []
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for i in range(len(self.nodes)):
                for j in range(i+1, len(self.nodes)):
                    process = executor.submit(self.find_paths, self.nodes[i], self.nodes[j])
                    processes.append(process)
            for f in concurrent.futures.as_completed(processes):
                paths = paths + f.result()

        return paths


def split_list(alist, parts):
    length = len(alist)
    return [ alist[i*length // parts: (i+1)*length // parts] for i in range(parts)]

def check_list(alist):
    words = []
    for i in alist:
        if wordcheck.check(i) and len(i) > 2 and i not in words:
            words.append(i)

    return words



time1 = time.time()
boggle = Graph()

wordlist = []

with concurrent.futures.ProcessPoolExecutor() as executor:
    for li in split_list(boggle.all_combinations(), multiprocessing.cpu_count()):
        process = executor.submit(check_list, li)
        wordlist.append(process)

    for f in concurrent.futures.as_completed(wordlist):
        print(f.result())



seconds = time.time() - time1
print('it took ' + str(seconds//60) + ' minutes')
