from heapq import heappop, heappush

class HuffNode():
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, hn):
        return self.freq < hn.freq


class HuffCoder():
    def __init__(self):
        self.clear_text_message = ''
        self.encoded_message = ''
        self.char_freq = {}
        self.min_heap = []
        self.huff_tree_root = None
        self.huff_code_table = {}


    def build_huff_tree(self):
        while len(self.min_heap) > 1:
            left_n = heappop(self.min_heap)
            right_n = heappop(self.min_heap)
            inner_n = HuffNode('', left_n.freq + right_n.freq)
            inner_n.left = left_n
            inner_n.right = right_n
            heappush(self.min_heap, inner_n)

        self.huff_tree_root = heappop(self.min_heap)


    def build_char_freq_dict(self, message):
        for c in message:
            self.char_freq[c] = self.char_freq.get(c, 0) + 1


    def populate_min_heap(self):
        for char, freq in self.char_freq.items():
            heappush(self.min_heap, HuffNode(char, freq))


    def build_huff_code_table(self, node, h_code=''):
        if len(self.char_freq) <= 1: # special case when input message consists only of single variety of char
            self.huff_code_table[node.char] = '0'
            return
    
        if node.left:
            self.build_huff_code_table(node.left, h_code + '0')

        if node.right:
            self.build_huff_code_table(node.right, h_code + '1')

        if node.char != '':
            self.huff_code_table[node.char] = h_code

        
    def encode(self, message):
        if message == '':
            return None
        self.build_char_freq_dict(message)
        self.populate_min_heap()
        self.build_huff_tree()
        self.build_huff_code_table(self.huff_tree_root)

        self.encoded_message = ''
        for char in message:
            self.encoded_message += self.huff_code_table[char]

        return self.encoded_message


    def decode(self):
        if self.huff_tree_root == None:
            return ''
        decoded_message = '' 
        current_node = self.huff_tree_root
        for c in self.encoded_message:
            if c == '0':
                if current_node.left:
                    current_node = current_node.left
            else:
                if current_node.right:
                    current_node = current_node.right
        
            if current_node.char != '':
                decoded_message += current_node.char
                current_node = self.huff_tree_root

        return decoded_message

     
        

# test case 1 -> 'regular' type of message
hc = HuffCoder()
message = 'AAAAAAABBBCCCCCCCDDEEEEEE'
hc.encode(message)
assert(message == hc.decode())

# test case 2 -> empty string message
hc = HuffCoder()
message = ''
hc.encode(message)
assert(message == hc.decode())

# test case 3 -> single variety char single frequency
hc = HuffCoder()
message = 'A'
hc.encode(message)
assert(message == hc.decode())

# test case 4 -> single variety char multy frequency
hc = HuffCoder()
message = 'AAAAAAAAAAAAAAAAAAAA'
hc.encode(message)
assert(message == hc.decode())
