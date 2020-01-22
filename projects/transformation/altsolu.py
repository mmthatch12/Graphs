from util import Stack

# this was a 
def dfs(begin_word, end_word):
    stack = Stack()
    stack.push([begin_word])

    while stack.size() > 0:

        sequence = stack.pop()
        print("sequence", sequence)

        last_word = sequence[-1]
        print("last_word", last_word)

        if last_word == end_word:
            return sequence
        
        possible_word = str(last_word)

        possible_list = list(possible_word)

        new_sequence = list(sequence)

        for letter in range(0, len(end_word)):
            possible_list[letter] = end_word[letter]
            new_possible = "".join(possible_list)

            print('new_SEQ', new_sequence)
            with open('words.txt') as f:
                if f'{new_possible}' in f.read():
                    new_sequence.append(new_possible)
                    stack.push(new_sequence)
    return None

print(dfs("sail", "boat"))