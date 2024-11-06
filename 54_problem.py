#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
test = Solution()
print(test.spiralOrder(a))
print(test.spiralOrder(b))
    