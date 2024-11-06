# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def  __init__(self) -> None:
        pass

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = None
        temp2 = head
        
        while temp2:
            temp3 = temp2.next
            temp2.next = temp1
            
            temp1 = temp2
            temp2 = temp3
        return temp1  

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

printNode(a)

test = Solution()
c = test.reverseList(a)

printNode(c)