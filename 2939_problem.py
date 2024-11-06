#

class Solution:

    def __init__(self) -> None:
        pass

    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        modul = pow(10,9) + 7
        bt = 1 << n
        
        while bt > 0:
            bt >>= 1
            if a * b < (a ^ bt) * (b ^ bt):
                a ^= bt
                b ^= bt
        return a * b % modul

a = 6
b = 7
n = 5
test = Solution()
print(test.maximumXorProduct(a,b,n))
    