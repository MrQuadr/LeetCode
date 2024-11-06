#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def setZeroes(self, matrix: List[List[int]]) -> None:
        columns = [False] * len(matrix[0])
        rows = [False] * len(matrix)

        for i, x in enumerate(matrix):
            for j, y in enumerate(x):
                if y == 0:
                    columns[j] = True
                    rows[i] = True
        
        for i, x in enumerate(rows):
            for j, y in enumerate(columns):
                if y or x:
                    matrix[i][j] = 0
        
        return matrix


a = [[1,1,1],[1,0,1],[1,1,1]]
b = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
test = Solution()
print(test.setZeroes(a))
print(test.setZeroes(b))
    