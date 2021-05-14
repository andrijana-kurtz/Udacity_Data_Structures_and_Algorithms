import time
from hashlib import sha256

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def __repr__(self):
        rep_d = {'timestap': self.timestamp,
                 'data': self.data,
                 'previous_hash': self.previous_hash.hexdigest(),
                 'hash': self.hash.hexdigest()}
        return f'{rep_d}'

    def calc_hash(self):
        h = sha256()
        h.update(self.timestamp.encode('utf-8'))
        h.update(self.data.encode('utf-8'))
        h.update(self.previous_hash.digest())

        return h

    def get_hash(self):
        return self.hash.hexdigest()

class Blockchain():

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        self.iblock = self.head
        return self

    def __next__(self):
        if self.iblock:
            block = self.iblock
            self.iblock = self.iblock.next
            return block
        else:
            raise StopIteration

    def __repr__(self):
        return f'{[b for b in self]}'

    def add(self, data):
        gmt_ts = time.strftime('%H:%M %m/%d/%Y', time.gmtime())

        if self.tail is None: # first block insertion
            self.head = Block(gmt_ts, data, sha256(b'0'))
            self.tail = self.head
            return

        block = Block(gmt_ts, data, self.tail.hash)
        self.tail.next = block
        self.tail = block

def test_hash_history(bc):
    '''
    test hash<-previous_hash 'link' between blocks
    '''
    for i, block in enumerate(bc):
        if i == 0:
            previous_hash = block.hash
            continue
    
        assert(previous_hash == block.previous_hash)
        previous_hash = block.hash

bc = Blockchain()
assert(repr(bc) == '[]') # test empty blockchain
print(f'empty blockchain:\n {bc}\n')

bc.add('p1')
test_hash_history(bc) # test with single block in blockchain
print(f'blockchain with single block:\n {bc}\n')

bc.add('p2')
bc.add('p3')
test_hash_history(bc) # test with b>1 blocks in blockchain
print(f'blockchain with three blocks:\n {bc}\n')

