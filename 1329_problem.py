#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        if row < 2 or col < 2:
            return mat
        
        

        return mat

a = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
test = Solution()
print(test.diagonalSort(a))
    