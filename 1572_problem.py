#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def diagonalSum(self, mat: List[List[int]]) -> int:
        summarum = 0
        i = 0
        j = len(mat) - 1

        for k in mat:
            if i != j:
                summarum += k[i]
                summarum += k[j]
            else:
                summarum += k[i]
            i += 1
            j -= 1

        return summarum
        # summarum = 0
        # i = 0
        # j = len(mat) - 1

        # while i < j:
        #     summarum += mat[i][i]
        #     summarum += mat[i][j]
        #     summarum += mat[j][i]
        #     summarum += mat[j][j]
        #     i += 1
        #     j -= 1
        
        # if i == j:
        #     summarum += mat[i][i]
        
        # return summarum


        
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
b = [[1,1,1,1],
     [1,1,1,1],
     [1,1,1,1],
     [1,1,1,1]]
c = [[5]]
test = Solution()
print(test.diagonalSum(a))
print(test.diagonalSum(b))
print(test.diagonalSum(c))
    