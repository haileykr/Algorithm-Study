"""
Remove Kth Node From End
10/13/2021
"""
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
# O(N) T, O(1) S
def removeKthNodeFromEnd(head, k):
    # two ptrs needed, k apart from each other
    ptr1, ptr2 = head, head
    while k > 0:
        ptr1 = ptr1.next
        k -= 1
    if ptr1 is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while ptr1.next is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    ptr2.next = ptr2.next.next
# O(N) T, O(1) S
# def removeKthNodeFromEnd(head, k):
#     counter = 1
#     first, second = head, head
#     while counter <= k:
#         second = second.next
#         counter += 1
#     if second is None:
#         head.value = head.next.value
#         head.next = head.next.next
#         return
#     while second.next is not None:
#         second = second.next
#         first = first.next
#     # because the second ptr is pointing the last value
#     # the first ptr is pointing the node right before the one to be removed!
#     first.next = first.next.next
