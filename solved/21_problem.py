# 21. Merge Two Sorted Lists -> https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def  __init__(self) -> None:
        pass

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tempNode = head = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                tempNode.next = list1
                list1 = list1.next
            else:
                tempNode.next = list2
                list2 = list2.next
            tempNode = tempNode.next
        
        tempNode.next = list1 if list1 else list2

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

if __name__ == "__main__":
    a = convertNode([1,2,4])
    b = convertNode([1,3,4])

    printNode(a)
    printNode(b)

    test = Solution()
    c = test.mergeTwoLists(a,b)

    printNode(c)