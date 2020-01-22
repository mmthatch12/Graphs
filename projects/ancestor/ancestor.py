from util import Stack, Queue

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")
    
    def find_parents(self, vertex_id):
        for vert in self.vertices:
            if vertex_id in self.vertices[vert]:
                return vert
    
def earliest_ancestor(ancestors, starting_node):
    graphy = Graph()
    for vert in ancestors:
        graphy.add_vertex(vert[0])
        graphy.add_vertex(vert[1])
    for edge in ancestors:
        graphy.add_edge(edge[0], edge[1])
    stack = Stack()
    stack.push(starting_node)

    visited = []
    while stack.size() > 0:
        vertex = stack.pop()
        if vertex not in visited and vertex is not None:
            visited.append(vertex)
            parent = graphy.find_parents(vertex)
            stack.push(parent)
    if visited[-1] == starting_node:
        return -1
    else:
        return visited[-1]

print('early')
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 6)



    