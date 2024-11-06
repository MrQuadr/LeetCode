#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # y = k * x + c
        x_0 = coordinates[0][0]
        y_0 = coordinates[0][1]
        x_interval = coordinates[1][0] - x_0
        y_interval = coordinates[1][1] - y_0

        for x, y in coordinates[2:]:
            if x_interval * (y - y_0) != y_interval * (x - x_0):
                return False
        # if x_interval == 0:
        #     for i in coordinates:
        #         if i[0] != x_0:
        #             return False
        # elif y_interval == 0:
        #     for i in coordinates:
        #         if i[1] != y_0:
        #             return False
        # else:
        #     k = y_interval / x_interval
        #     c = y_0 - k * x_0

        #     for i in coordinates[2:]:
        #         temp = k * i[0] + c
        #         if temp != i[1]:
        #             return False
        
        return True


a = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
b = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
c = [[0,0],[0,1],[0,-1]]
d = [[2,4],[2,5],[2,8]]
test = Solution()
print(test.checkStraightLine(a))
print(test.checkStraightLine(b))
print(test.checkStraightLine(c))
print(test.checkStraightLine(d))
    