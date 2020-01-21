"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # *******BRADY SAID i SHOULD MEMORIZE THIS!!
        # Create an empty queue and enqueue the starting vertex ID
        queue = Queue()
        queue.enqueue(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # while the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first vertex
            vert = queue.dequeue()
            # if that vertex has not been visited..
            if vert not in visited:
                # Mark it as visited
                print(vert)
                visited.add(vert)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.get_neighbors(vert):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
         # *******BRADY SAID i SHOULD MEMORIZE THIS!!
        # Create an empty stack and push the starting vertex ID
        stack = Stack()
        stack.push(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # while the stack is not empty...
        while stack.size() > 0:
            # pop the first vertex
            vert = stack.pop()
            # if that vertex has not been visited..
            if vert not in visited:
                # Mark it as visited
                print(vert)
                visited.add(vert)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.get_neighbors(vert):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        
        def inner_dft():
            if stack.size() < 1:
                return 
            else:
                vert = stack.pop()
                if vert not in visited:
                    print(vert)
                    visited.add(vert)
                    for neighbor in self.get_neighbors(vert):
                        stack.push(neighbor)
                    return inner_dft()
        return inner_dft()

        # Brians solution
        # def dft_recursive(self, starting_vertex, visited=None):
        # """
        # Print each vertex in depth-first order
        # beginning from starting_vertex.

        # This should be done using recursion.
        # """
        # if visided is None:
            # visited = set()
        # visited.add(start_vert)
        # print(starting_vertex)
        # for child_vert in self.vertices[starting_vertex]:
            # if child_vert not in visited:
                # self.dft_recursive(child_vert, visited)




    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        short  = []

        while queue.size() > 0:
            vert = queue.dequeue()
            if vert == destination_vertex:
                short.append(vert)
                return short
            elif vert not in visited:
                print(vert)
                visited.add(vert)
                short.append(vert)
                for neighbor in self.get_neighbors(vert):
                    queue.enqueue(neighbor)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
         # *******BRADY SAID i SHOULD MEMORIZE THIS!!
        # Create an empty stack and push the starting vertex ID
        stack = Stack()
        # Enstack a list to use as our path
        stack.push([starting_vertex])
        # Create an empty Set to store visited vertices
        visited = set()
        # while the stack is not empty...
        while stack.size() > 0:
            # pop the first vertex
            path = stack.pop()
            vert = path[-1]
            # if that vertex has not been visited..
            if vert not in visited:
                # Mark it as visited
                if vert == destination_vertex:
                    #Do the thing
                    return path
                visited.add(vert)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.get_neighbors(vert):
                    # copy path to avoid pass by reference bug
                    new_path = list(path) # Make a copy of path rather than reference
                    new_path.append(neighbor)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == target_value:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
