#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        for i, j in zip(target, arr):
            if i != j:
                return False
        return True

a = [630,262,255,927,255,924,310,872,492,750,376,651,312,445,238,330,149,604,714,48,852,444]
b = [444,927,48,924,262,376,852,238,872,630,310,492,149,255,651,255,750,604,445,330,312,714]
test = Solution()
print(test.canBeEqual(a, b))
    