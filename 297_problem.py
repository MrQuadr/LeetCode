# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def __init__(self) -> None:
        self.sbl = "_"
        pass

    def serialize(self, root: Optional[TreeNode]) -> str:
        temp_str = ''
        if root:
            temp_str += str(root.val) + self.sbl
            temp_str += self.serialize(root.left)
            temp_str += self.serialize(root.right)
        
        return temp_str
        

    def deserialize(self, data, size=None) -> TreeNode:
        print(data)
        tempNode = None
        if size == None:
            data = data.split(self.sbl)
            size = len(data) >> 1
        else:
            size >>= 1

        if size > 0:
            tempNode = TreeNode(data[0])
            tempNode.left = self.deserialize(data[1:size],size)
            tempNode.right = self.deserialize(data[size:],size)
        
        return tempNode
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

def convertTreeNode(l: Optional[list], c=0, s=0):
    if s == 0:
        s = len(l)
    
    if c < s:
        t = TreeNode(l[c])
        t.left = convertTreeNode(l, (2*c+1), s)
        t.right = convertTreeNode(l, (2*c+2), s)
        return t
    else:
        return None

a = convertTreeNode([1,2,3,None,None,4,5,None,None,None,None,6,7,8,None])

test = Codec()
c = test.serialize(a)
print(c)
c = test.deserialize(c)
c = test.serialize(c)
print(c)