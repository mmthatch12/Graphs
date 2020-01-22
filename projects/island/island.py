# Write a function that takes a 2D binary
# array and returns the number of 1 islands.
# An island consists of 1s that are connected
# to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4
# connected - has edges, connected components
# array/2d
#n, s, e, w
#binary - values
#island/1 islands = connected components
#  return 1 islands - number of connect components
# from graph import Graph
# from util import Stack, Queue

# graph = Graph()

# for island in islands:
#     for ind in island:
#         graph.add_vertex((island.index(), ind.index()))
