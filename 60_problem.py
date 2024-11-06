#

class Solution:

    def __init__(self) -> None:
        pass

    def getPermutation(self, n: int, k: int) -> str:
        temp = ''.join([f'{(i+1)}' for i in range(n)])
        result = ''
        f = 1
        fact = 1
        while f < k:
            fact += 1
            f *= fact
        
        f //= fact
        fact -= 1

        while fact
            
        
        


        
        

        return result

n = 3
k = 3
test = Solution()
print(test.getPermutation(n, k))