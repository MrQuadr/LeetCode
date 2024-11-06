#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # list_sum = [sum(i) for i in accounts]
        # list_sum.append(0)
        # return max(*list_sum)

        max_acc = 0
        for i in accounts:
            max_acc = max(max_acc, sum(i))
        return max_acc

a = [[2,8,7],[7,1,3],[1,9,5]]
test = Solution()
print(test.maximumWealth(a))
    