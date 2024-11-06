#

class Solution:

    def __init__(self) -> None:
        pass

    def reverse(self, x: int) -> int:
        y = 0
        corr = 1

        if x < 0:
            corr = -1
            x *= corr
        
        while x > 0:
            y *= 10
            y += x % 10
            x //= 10
        
        if (y >> 31) > 0:
            y = 0
        
        return y * corr
