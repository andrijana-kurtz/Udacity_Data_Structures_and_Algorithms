Efficiency
There is a clear and accurate statement of efficiency. There is an explanation that specifically mentions parts of the code that contribute to the overall efficiency.


- Analysis for insert and find methods of class Trie
  Time efficiency: O(n) where n is number of letters for given word/prefix
                        - time dominating code is present in insert and find methods of Trie class
                          more specifically this is a traversal code common for both methods:

                              for c in path_list:
                                  if c not in node.children:
                                      ...
                                  node = node.children[c]

                          which is resulting with O(n) time efficiency

  Space efficiency: O(n) where n is number of nodes after path is parsed
                         - worst case is that we could have all unique paths with non overlapping nodes
                         - space efficiency for find method is O(1)


- Analysis for suffixes (and associated helper) method of TrieNode
  Time efficiency is O(m): where m is the number of nodes in subtree under the last node of given suffix.
  Space efficiency - O(s): where s is the number of found suffixes which I store in additional suff_store python list. 


Code Design
Explanation contains some discussion of design choices made in the code. Some examples include the choice of algorithm and data structure.

- For Trie and prefix search I've built upon code from udacity lessons. Suffixes method on TrieNode class does DFS recursively to find words and store them in suff_store python list.
