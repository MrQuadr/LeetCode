#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix[0])
        st, limit = 0, len(matrix) * row - 1

        while st <= limit:
            index = (st + limit) >> 1
            x, y = index // row, index % row
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                st = index + 1
            else:
                limit = index - 1

        return False

a = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
b = 5
test = Solution()
print(test.searchMatrix(a, b))
    