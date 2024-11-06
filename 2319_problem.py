#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        len_grid = len(grid) - 1
        for i, x in enumerate(grid):
            k = len_grid - i
            for j, y in enumerate(x):
                if y == 0:
                    if j == i or j == k:
                        return False
                else:
                    if j != i and j != k:
                        return False
        
        return True

a = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
test = Solution()
print(test.checkXMatrix(a))
    