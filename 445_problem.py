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
        head = temp = ListNode()
        n1 = 0
        n2 = 0

        while l1:
            n1 *= 10
            n1 += l1.val
            l1 = l1.next
        
        while l2:
            n2 *= 10
            n2 += l2.val
            l2 = l2.next
        
        n1 += n2

        if n1 == 0:
            head.val = n1
            return head

        while n1 > 0:
            head = ListNode()
            temp.val = n1 % 10
            head.next = temp
            temp = head
            n1 //= 10

        return head.next

def convertNode(l: Optional[list]):
    t = None
    c = len(l) - 1
    for i in range((c+1)):
        t = ListNode(l[c-i],t)
    return t

def printNode(l: Optional[ListNode]):
    i = 0
    while l and i < 100:
        t = "\n" if l.next == None else " -> "
        print(l.val, end=t)
        l = l.next
        i+= 1

a = convertNode([0])
b = convertNode([0])

printNode(a)
printNode(b)

test = Solution()
c = test.addTwoNumbers(a,b)

printNode(c)