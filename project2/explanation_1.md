Efficiency: There is a clear and accurate statement of efficiency in time and space. There is an explanation that specifically mentions parts of the code that contribute to the overall efficiency.

Time eff: O(1)
Since requirement of this problem is that all operations have to be O(1), I chose to build on OrderedDict datastructure since it provides required time efficiency.

Space eff: O(n)
Using OrderedDict datastructure to store cached items, n is number of cached items and is controlled by given capacity value.


Code Design: Explanation contains some discussion of design choices made in the code. Some examples include the choice of algorithm and data structure.
Since requirement of this problem is that all operations have to be O(1), I chose to build on OrderedDict datastructure since it provides required time efficiency. -> https://github.com/python/cpython/blob/df9ade9beb86935963f8ae47d9377578399ab6d2/Objects/odictobject.c#L23
Idea is simple since ordered dict preserves insertion order, on set and get operations we can update cache item 'age' by inserting it at the 'end' of dictionary. On insertion we validate if we are at capacity, and if so we expell 'oldest' or 'first' item in our OrderedDict datastruct. 

Readability: Explanation is written with proper English. Wording is clear and easy to understand. It’s okay to make a couple mistakes, but thoughts should be clearly expressed overall.
