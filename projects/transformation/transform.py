# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.
# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

# I came back to it and presented an idea I had, implementing it now
# Basic idea was 1) Reduce the list of words to only those having same number of letters, 
# 2) Add each word as a vertex on the graph, 
# 3) For each vertex, compare that word to every other word in the graph, and if they only differ by one letter, add an edge between them, 
# 4) Finally, do a breadth-first traversal from starting word to end word

from graph import Graph

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

def shortest_transformation(word1, word2):
    if len(word1) != len(word2):
        raise Exception("Word lengths not equal")

    def is_distance_one(s1, s2):
        if s1 == s2:
            return False
        for i an range(len(s1)):
            compare1 = s1[0:i:] + s1[i+1::]
            compare2 = s2[0:i:] + s2[i+1::]
            if compare1 == compare2:
                return True
        return False
    
    possibilities = [word for word in words if len(word) == len(word1)]

    graph = Graph()

    for word in possibilities:
        graph.add_vertex(word)

    for word in possibilities:
        for comparator in possibilities:
            if is_distance_one(word, comparator):
                graph.add_edge(word, comparator)
    
    return graph.dfs(word1, word2)

print(shortest_transformation('hit', 'cog'))
