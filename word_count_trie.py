#! Q2 Improved answer for Q1 using trie.
'''
# Trie - A trie is a tree-like data structure that allows for efficient
#  prefix searching of words. In the context of counting word occurrences,
#  we can use a trie to store each unique word in the text.
# The nodes in the trie can store a count of the number of times the associated word has been seen.
# To count the occurrences of each word, we can traverse the trie and sum up the counts at each leaf node.


# I am using the sort in Q1,
# and then count the number of occurrences of each word.
# This can be more efficient than using a trie
# if the number of unique words in the text is relatively small.
'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word_count += 1

    def count_words(self, filename):
        with open(filename, 'r') as file:
            text = file.read().lower().replace('\n', ' ')
            words = text.split()
            for word in words:
                self.insert(word)
        return self.get_word_count()

    def get_word_count(self):
        word_count = {}
        stack = [(self.root, "")]
        while stack:
            node, prefix = stack.pop()
            if node.word_count > 0:
                word_count[prefix] = node.word_count
            for char, child in node.children.items():
                stack.append((child, prefix + char))
        return word_count

    # Example usage


def run_counter():
    trie = Trie()
    word_count = trie.count_words('sample.txt')
    for word, count in word_count.items():
        print(f'{word}: {count}')
    '''
    The TrieNode class represents a node in the Trie data structure.
      It has a dictionary children that maps each character to its child node and an
      integer word_count that stores the number of times the word ending at this node has been seen.
    The Trie class represents a Trie data structure. It has a root node that is initialized
      in the constructor and methods to insert words into the Trie
      and count the occurrences of each word in a text file.
    The insert() method inserts a word into the Trie by iterating through each character of
      the word and adding a new child node if it doesn't exist.
    The count_words() method reads a text file into a string, splits the string into words,
      and inserts each word into the Trie using the insert() method.
      It then returns a dictionary containing the counts of each word in the Trie by calling the get_word_count() method.
    The get_word_count() method traverses the Trie in a depth-first manner using a stack and returns
      a dictionary containing the counts of each word ending at a leaf node in the Trie.
    In the example usage, we create a new instance of the Trie class and call
      the count_words() method with the filename sample.txt.
      We then print the word count for each word in the text file.

    '''


if __name__ == '__main__':
    run_counter()
