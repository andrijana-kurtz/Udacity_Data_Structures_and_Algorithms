Efficiency: There is a clear and accurate statement of efficiency in time and space. There is an explanation that specifically mentions parts of the code that contribute to the overall efficiency.

Time eff:

methods:
  - self.build_char_freq_dict(message) O(n) - where n is number of chars from input message
  - self.populate_min_heap() O(c) where c is character/key from freq. table
  - self.build_huff_tree() O(c)
  - self.build_huff_code_table(self.huff_tree_root) 0(c)

Overall time complexity is O(n logn)

Space eff:
In addition to keeping input message O(n), I also keep few datastructures required to execute huffman encoding algorithm;
  - Dictionary to count char frequency in input message - O(c) - where c is character/key from freq. table
  - Minimum heap as aux DS used to build huffman tree - O(c)
  - Huffman Tree - O(c)
  - Dictionary - huffman code table used for quick lookup during encode - O(c)

Since I'm using string to represent all (input, encoded and decoded) messages, encoded message O(e) will always be >= than input O(n) or decoded message.

Code Design: Explanation contains some discussion of design choices made in the code. Some examples include the choice of algorithm and data structure.
I've already described fair bit in time and space efficiency analysis above. I followed huffman algorithm as described in problem specification. For simplicity and reasoning I broke up encode method into multiple steps - methods.

Possible optimization: currently all messages (input, encoded, decoded) are stored as strings. Since we are encoding with binary (0, 1), to reduce space use, encoded messages should be stored as bitarrays (https://wiki.python.org/moin/BitArrays) i.e.

Readability: Explanation is written with proper English. Wording is clear and easy to understand. It’s okay to make a couple mistakes, but thoughts should be clearly expressed overall.
