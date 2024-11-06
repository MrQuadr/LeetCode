# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def  __init__(self) -> None:
        pass

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = tempNode = ListNode()
        value = 0

        while l1 or l2 or value:
            tempNode.next = ListNode()
            tempNode = tempNode.next
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            tempNode.val = value % 10 
            value = value // 10
        return head.next

def convertNode(l: Optional[list]):
    t = None
    c = len(l) - 1
    for i in range((c+1)):
        t = ListNode(l[c-i],t)
    return t

def printNode(l: Optional[ListNode]):
    while l:
        t = "\n" if l.next == None else " -> "
        print(l.val, end=t)
        l = l.next

a = convertNode([1,2,4])
b = convertNode([1,3,4])

printNode(a)
printNode(b)

test = Solution()
c = test.addTwoNumbers(a,b)

printNode(c)
        