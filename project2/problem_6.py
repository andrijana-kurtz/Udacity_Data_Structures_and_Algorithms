"""
Union and Intersection of Two Linked Lists

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        self.node = self.head
        return self

    def __next__(self):
        if self.node:
            node = self.node
            self.node = self.node.next
            return node
        else:
            raise StopIteration

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    set1 = {n.value for n in llist_1}
    set2 = {n.value for n in llist_2}
    union = set1.union(set2)
    result_llist = LinkedList()
    for value in union:
        result_llist.append(value)
    return result_llist

def intersection(llist_1, llist_2):
    set1 = {n.value for n in llist_1}
    set2 = {n.value for n in llist_2}
    isec = set1.intersection(set2)
    result_llist = LinkedList()
    for value in isec:
        result_llist.append(value)
    return result_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

assert(str(union(linked_list_1,linked_list_2)) == '32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> ')
assert(str(intersection(linked_list_1,linked_list_2)) == '4 -> 21 -> 6 -> ')

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

assert(str(union(linked_list_3,linked_list_4)) == '65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> ')
assert(str(intersection(linked_list_3,linked_list_4)) == '')

# Test case 3 - Two empty lists

linked_list_A = LinkedList()
linked_list_B = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_A.append(i)

for i in element_2:
    linked_list_B.append(i)

assert(str(union(linked_list_A,linked_list_B)) == '')
assert(str(intersection(linked_list_A,linked_list_B)) == '')


# Test case 4 - Two lists, of which one empty

linked_list_A = LinkedList()
linked_list_B = LinkedList()

element_1 = [1,2,3,4]
element_2 = []

for i in element_1:
    linked_list_A.append(i)

for i in element_2:
    linked_list_B.append(i)

assert(str(union(linked_list_A,linked_list_B)) == '1 -> 2 -> 3 -> 4 -> ')
assert(str(intersection(linked_list_A,linked_list_B)) == '')


# Test case 5 - Two same lists

linked_list_A = LinkedList()
linked_list_B = LinkedList()

element_1 = [1,2,3,4]
element_2 = [1,2,3,4]

for i in element_1:
    linked_list_A.append(i)

for i in element_2:
    linked_list_B.append(i)

assert(str(union(linked_list_A,linked_list_B)) == '1 -> 2 -> 3 -> 4 -> ')
assert(str(intersection(linked_list_A,linked_list_B)) == '1 -> 2 -> 3 -> 4 -> ')

# Test case 5 - Two same lists

linked_list_A = LinkedList()
linked_list_B = LinkedList()

element_1 = [2,2,2]
element_2 = [3,3,3]

for i in element_1:
    linked_list_A.append(i)

for i in element_2:
    linked_list_B.append(i)

assert(str(union(linked_list_A,linked_list_B)) == '2 -> 3 -> ')
assert(str(intersection(linked_list_A,linked_list_B)) == '')



