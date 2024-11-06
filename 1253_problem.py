#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        out_list = [0] * len(colsum)

        for i, j in enumerate(colsum):
            if j == 1:
                if upper >= lower:
                    out_list[i] = 1
                    colsum[i] = 0
                    upper -= 1
                else:
                    lower -= 1
            else:
                if j == 2:
                    out_list[i] = 1
                    colsum[i] = 1
                    upper -= 1
                    lower -= 1
                else:
                    colsum[i] = 0
        
        if upper != 0 or lower != 0:
            return []
        return [out_list, colsum]

a = 2
b = 1
c = [1,1,1]
test = Solution()
print(test.reconstructMatrix(a, b, c))
    