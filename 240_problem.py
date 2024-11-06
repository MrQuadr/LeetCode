#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        col = len(matrix[0])-1
        row = len(matrix)
        
        while i < row and col >= 0:
            if matrix[i][col] == target:
                return True

            if matrix[i][col] > target:
                col -= 1
            else:
                i += 1

        return False

a = [[1,4],[2,5]]
b = 0
test = Solution()
print(test.searchMatrix(a, b))