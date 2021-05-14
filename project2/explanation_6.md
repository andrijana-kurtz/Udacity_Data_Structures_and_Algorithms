Efficiency: There is a clear and accurate statement of efficiency in time and space. There is an explanation that specifically mentions parts of the code that contribute to the overall efficiency.

Time eff: O(a+b)
For time efficiency in case of both functions (union and intersection), we have to read through all nodes of both linked lists,since lists can be of different sizes I chouse to denote number of nodes with a and b.

Space eff: O(a+b+c)
Same as with time efficiency, linked lists can be of different size hence number of nodes is denoted as a and b, additionally I'm storing resulting linked with c number of nodes.

Code Design: Explanation contains some discussion of design choices made in the code. Some examples include the choice of algorithm and data structure.
Since in specification of this problem there were no requirements as to what time and space efficiency should be, I opted to use pythons built-in set datastructure. Nodes from each linked list are loaded into respective set, and required set operation is performed on them, resulting in new set which in turn is loaded into returned resulting linked list. 

Readability: Explanation is written with proper English. Wording is clear and easy to understand. It’s okay to make a couple mistakes, but thoughts should be clearly expressed overall.
