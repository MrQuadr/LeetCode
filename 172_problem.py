#

class Solution:

    def __init__(self) -> None:
        pass

    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n != 0:
            n //= 5
            result += n
        
        return result

a = 4
test = Solution()
print(test.trailingZeroes(a))