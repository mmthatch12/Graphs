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
    

graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_vertex(8)
graph.add_vertex(9)
graph.add_vertex(10)
graph.add_vertex(11)
graph.add_edge(10, 1)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 6)
graph.add_edge(4, 5)
graph.add_edge(4, 8)
graph.add_edge(5, 6)
graph.add_edge(5, 7)
graph.add_edge(11, 8)
graph.add_edge(8, 9)


print(graph.vertices)

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
            print(vertex)
            visited.append(vertex)
            parent = graphy.find_parents(vertex)
            stack.push(parent)
    print('graphy.vertices', graphy.vertices)
    if visited[-1] == starting_node:
        return -1
    else:
        return visited[-1]

print('early')
earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6)



    