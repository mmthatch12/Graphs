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
