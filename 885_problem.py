#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        out_list = [[rStart, cStart]]
        limit_all = rows * cols
        limit, i, j = 1,1,1
        route = 1
        flag = True

        while limit_all > 1:
            if flag:
                cStart += route
                i -= 1
                if i == 0:
                    flag = False
                    j = limit
                    limit += 1
            else:
                rStart += route
                j -= 1
                if j == 0:
                    flag = True
                    route = -route
                    i = limit
            
            if (0 <= rStart < rows) and (0 <= cStart < cols):
                out_list.append([rStart, cStart])
                limit_all -= 1

        return out_list



a = 1
b = 4
c = 0
d = 0
test = Solution()
print(test.spiralMatrixIII(a,b,c,d))
    