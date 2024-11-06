#

class Solution:

    def __init__(self) -> None:
        pass

    def mySqrt(self, x: int) -> int:
        if x < 0:
            return 0
        elif x < 2:
            return x
        else:
            y = self.mySqrt(x >> 2) << 1
            z = y + 1
            if z * z > x:
                return y
            else:
                return z



a = 1000
test = Solution()
print(test.mySqrt(a))
    