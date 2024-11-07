# 60. Permutation Sequence -> https://leetcode.com/problems/permutation-sequence/description/

class Solution:

    def __init__(self) -> None:
        pass

    def getPermutation(self, n: int, k: int) -> str:
        temp = ''.join([f'{(i+1)}' for i in range(n)])
        result = ''

        f = 1
        for i in range(1, n):
            f *= i
        
        for i in range(1, n):
            x = k // f
            print(k, f,x)
            k -= x*f
            f //= (n-i)

            result = ''.join([result, temp[x]])
            temp = temp.split(temp[x])
            temp = ''.join(temp)
        
        return ''.join([result, temp])

if __name__ == "__main__": 
    n = 3
    k = 3
    test = Solution()
    print(test.getPermutation(n, k))