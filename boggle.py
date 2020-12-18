import enchant

wordcheck = enchant.Dict('en_US')

grid = [
     ['p', 's', 'a', 'a'],
    ['a', 'p', 'w', 'i'],
    ['p', 'o', 'e', 'b'],
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

    def get_children(self):
        return [i.data for i in self.children]

class Graph:
    def __init__(self, grid):
        self.grid = grid
        self.nodes = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid)):
                self.nodes.append(Node(grid[y][x], [y, x]))

        def get_surrounding(self):
            surrounding = [grid[y+1][x], grid[y-1][x], grid[y][x+1], grid[y][x-1], grid[y+1][x+1], grid[y-1][x-1], grid[y+1][x-1], grid[y-1][x+1]]
            if x == 0:
                surrounding.remove(grid[y][x-1])
                surrounding.remove(grid[y+1][x-1])
                surrounding.remove(grid[y-1][x-1])

            elif x == len(grid)-1:
                surrounding.remove(grid[y][x+1])
                surrounding.remove(grid[y+1][x+1])
                surrounding.remove(grid[y-1][x+1])

            if y == 0:
                surrounding.remove(grid[y-1][x])
                try:
                    surrounding.remove(grid[y-1][x-1])
                except:
                    pass
                try:
                    surrounding.remove(grid[y-1][x+1])
                except:
                    pass

            elif y == len(grid)-1:
                surrounding.remove(grid[y+1][x])
                try:
                    surrounding.remove(grid[y+1][x-1])
                except:
                    pass
                try:
                    surrounding.remove(grid[y+1][x+1])
                except:
                    pass

            return surrounding


        for i in self.nodes:
            i.add_child()

        for i in self.nodes:
            print(i.data)
            print(i.get_children())

    def add_all_children(self):
        pass

    def traverse(self, start, end):
        pass

    def all_paths(self):
        pass

    def find_all_paths(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                 newpaths = find_all_paths(graph, node, end, path)
                 for newpath in newpaths:
                    paths.append(newpath)
        return paths

boggle = Graph(grid)


'''
if y == 0 and x == 0:
 18               dic[grid[y][x]] = [grid[y+1][x], grid[y+1][x+1], grid[y][x+1]]
 19           elif y == 0 and x == len(grid)-1:
 20               dic[grid[y][x]] = [grid[y+1][x], grid[y+1][x-1], grid[y][x-1]]
 21           elif y == len(grid)-1 and x == 0:
 22               dic[grid[y][x]] = [grid[y-1][x], grid[y-1][x+1], grid[y][x+1]]
 23           elif y == len(grid)-1 and x == len(grid)-1:
 24               dic[grid[y][x]] = [grid[y-1][x], grid[y-1][x-1], grid[y][x-1]]
 25           #EDGES
 26
 27           elif y == len(grid)-1:
 28               dic[grid[y][x]] = [grid[y-1][x], grid[y][x+1], grid[y][x-1], grid[y-1][x+1], grid[y-1][x-1]]
 29           elif x == len(grid)-1:
 30               dic[grid[y][x]] = [grid[y+1][x], grid[y-1][x], grid[y][x-1], grid[y+1][x-1], grid[y-1][x-1]]
 31           elif y == 0:
 32               dic[grid[y][x]] = [grid[y+1][x], grid[y][x+1], grid[y][x-1], grid[y+1][x+1], grid[y+1][x-1]]
 33           elif x == 0:
 34               dic[grid[y][x]] = [grid[y+1][x], grid[y-1][x], grid[y][x+1], grid[y+1][x+1], grid[y-1][x+1]]
 35
 36           else:
 37               dic[grid[y][x]] = [grid[y+1][x], grid[y-1][x], grid[y][x+1], grid[y][x-1], grid[y+1][x+1], grid[y-1][x-1], grid[y+1][x-1], grid[y-1][x+1]]
'''
