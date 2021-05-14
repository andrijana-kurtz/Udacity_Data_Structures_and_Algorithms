Efficiency: There is a clear and accurate statement of efficiency in time and space. There is an explanation that specifically mentions parts of the code that contribute to the overall efficiency.

Time eff:
Since we are using linked list with tail pointer to store blocks and create blockchain add block operation is O(1) simple block insertion at tail.
Additionally I'm using iterator to go through all the blocks in blockchain, and that operation is O(n)

Space eff: O(n)
I'm storing O(n) blocks in blockchain.

Code Design: Explanation contains some discussion of design choices made in the code. Some examples include the choice of algorithm and data structure.
To deliver on problem spec I opted to use simple singly linked list with head and tail pointer. Tail pointer enables me to have O(1) for 'add' operation, basically inserting new block at the tail of linked list.
For hashing I'm mixing in; gmt based timestamp in format '%H:%M %m/%d/%Y' as proposed in problem spec(image), input block data and to further ensure hash uniqueness I also add in previous hash in it's encoded string digest representation.

I wrote also couple of tests to test empty, single block and more than single block blockchains, leveraging iterator I implemented in blockchain class.

Readability: Explanation is written with proper English. Wording is clear and easy to understand. It’s okay to make a couple mistakes, but thoughts should be clearly expressed overall.
