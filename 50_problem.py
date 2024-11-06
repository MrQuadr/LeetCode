#

class Solution:

    def __init__(self) -> None:
        pass

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            y = self.myPow(x, (-n))
            return 1/y
        elif n == 0:
            return 1
        elif n == 1:
            return x
        else:
            y = self.myPow(x, (n >> 1))
            y *= y
            if n & 1:
                y *= x
            return y

a = 2
b = 10
test = Solution()
print(test.myPow(a,b))
    