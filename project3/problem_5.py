"""
Building a Trie in Python

Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

    A Trie class that contains the root node (empty string)
    A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

Give it a try by implementing the TrieNode and Trie classes below!
"""

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def suffixes(self):
        suff_store = []
        self._suffixes_helper('', suff_store, self)
        return suff_store

    def _suffixes_helper(self, suffix, store, pnode):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point

        if self.is_word:
            store.append(suffix)

        for ck, node in self.children.items():
            if self == pnode:
                suffix = ''
            newsuffix = suffix + ck
            node._suffixes_helper(newsuffix, store, pnode)

        return store
            

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """
        insert `word` to trie
        """
        node = self.root
        for c in word:
            
            if c not in node.children:
                node.children[c] = TrieNode()
                
            node = node.children[c]
            
        node.is_word = True


    def find(self, prefix):
        node = self.root

        for c in prefix:
            if c not in node.children:
                return None

            node = node.children[c]

        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

node = MyTrie.find('tr')
print(node.suffixes())
assert(node.suffixes() == ['ie', 'igger', 'igonometry', 'ipod'])

node = MyTrie.find('ant')
print(node.suffixes())
assert(node.suffixes() == ['', 'hology', 'agonist', 'onym'])

node = MyTrie.find('f')
print(node.suffixes())
assert(node.suffixes() == ['un', 'unction', 'actory'])

node = MyTrie.find('') #edge case empty input prefix, I would personally expect all available words
print(node.suffixes())
assert(node.suffixes() == ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod'])

node = MyTrie.find('Slavko') #edge case non existing input prefix
assert(node == None)

