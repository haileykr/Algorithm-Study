"""
Linked List Construction
10/12/2021
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # O(1) TS
    def setHead(self, node):
        if self.head is None:  # empty doublylinkedlist
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)
    def setTail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)
    # O(1) TS
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None: #insert before head
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev= nodeToInsert
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None: #insert after tail
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next= nodeToInsert
    # O(P) T | O(1) S
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        ptr = self.head
        currPos = 1
        while ptr is not None and currPos != position:
            ptr = ptr.next
            currPos += 1
        if ptr is not None:
            self.insertBefore(ptr, nodeToInsert)
    # O(n) T | O(1) S
    def removeNodesWithValue(self, value):
        ptr = self.head
        while ptr is not None :
            nodeToRemove = ptr
            ptr = ptr.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
    # O(1) TS
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)
    # O(n) T | O(1) S
    def containsNodeWithValue(self, value):
        ptr = self.head
        while ptr != None:
            if ptr.value == value:
                return True
            ptr = ptr.next
        return False
    # O(1) TS
    def removeNodeBindings(self,node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
