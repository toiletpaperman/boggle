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

    def print_children(self):
        return [i.data for i in self.children]

    def get_surrounding_nodes(self):

        if self.y == 0 and self.x == 0:
            surrounding = [[1, 0], [1, 1], [0, 1]]
        elif self.y == 0 and self.x == len(grid)-1:
            surrounding = [[1, 0], [1, -1], [0, -1]]
        elif self.y == len(grid)-1 and self.x == 0:
            surrounding = [[-1, 0], [-1, 1], [0, 1]]
        elif self.y == len(grid)-1 and self.x == len(grid)-1:
            surrounding = [[-1, 0], [-1, -1], [0, -1]]
       #EDGES

        elif self.y == len(grid)-1:
            surrounding = [[-1, 0], [0, 1], [0, -1], [-1, 1], [-1,-1]]
        elif self.x == len(grid)-1:
            surrounding = [[1, 0], [-1, 0], [0, -1], [1, -1], [-1,-1]]
        elif self.y == 0:
            surrounding = [[1, 0], [0, 1], [0, -1], [1, 1], [1,-1]]
        elif self.x == 0:
            surrounding = [[1, 0], [-1, 0], [0, 1], [1, 1], [-1, 1]]

        else:
            surrounding = [[1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        final = list()

        for i in range(len(surrounding)):
            y = surrounding[i][0]
            x = surrounding[i][1]
            letter = grid[y+self.y][x+self.x]
            final.append(Node(letter, [y+self.y, x+self.x]))

        return final


class Graph:
    def __init__(self, grid):
        self.grid = grid
        self.nodes = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid)):
                self.nodes.append(Node(grid[y][x], [y, x]))
        for i in self.nodes:
            for j in i.get_surrounding_nodes():
                j.add_child(i)
            print(f'{i.data} --->  {i.print_children()}')

boggle = Graph(grid)


