"""
Sum of Linked Lists
10/13/2021
"""
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(n, m)) TS
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newListHead = LinkedList(0)
    newListPtr = newListHead
    value1, value2 = linkedListOne.value, linkedListTwo.value
    carry = 0
    listOneDone, listTwoDone = False, False
    while True:
        currSum = (value1 + value2 + carry) % 10
        carry = (value1 + value2 + carry) // 10
        newListPtr.value = currSum
        if linkedListOne.next is not None:
            linkedListOne = linkedListOne.next
            value1 = linkedListOne.value
        else:
            listOneDone = True
            value1 = 0
        if linkedListTwo.next is not None:
            linkedListTwo = linkedListTwo.next
            value2 = linkedListTwo.value
        else:
            listTwoDone = True
            value2 = 0
        if carry or not listOneDone or not listTwoDone:
            newListPtr.next = LinkedList(0)
            newListPtr = newListPtr.next
        else:
            break

    return newListHead

# O(max(n, m))TS
# def sumOfLinkedLists(linkedListOne, linkedListTwo):
# 	newLinkedListHeadPointer = LinkedList(0)
# 	currentNode= newLinkedListHeadPointer
# 	carry = 0
# 	nodeOne = linkedListOne
# 	nodeTwo = linkedListTwo
# 	while nodeOne is not None or nodeTwo is not None or carry != 0:
# 		valueOne = nodeOne.value if nodeOne is not None else 0
# 		valueTwo = nodeTwo.value if nodeTwo is not None else 0
# 		sumOfValues = valueOne + valueTwo +carry
# 		newVal = sumOfValues % 10
# 		newNode = LinkedList(newVal)
# 		currentNode.next = newNode
# 		currentNode = newNode
# 		carry = sumOfValues // 10
# 		nodeOne = nodeOne.next if nodeOne is not None else None
# 		nodeTwo = nodeTwo.next if nodeTwo is not None else None
# 	return newLinkedListHeadPointer.next
