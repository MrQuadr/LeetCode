#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def combine(self, n: int, k: int) -> List[List[int]]:
        k -= 1
        mask = [1 for i in range(k)]
        sum_mask = k
        result = []
        flag = True

        while flag:
            for i in range(n - sum_mask):
                result.append([i+1])
                for i in range(k):
                    result[-1].append(result[-1][-1] + mask[i])
            j = k - 1  
            while j >= 0:
                mask[j] += 1
                sum_mask += 1
                if sum_mask == n:
                    sum_mask -= mask[j]
                    sum_mask += 1
                    mask[j] = 1
                    j -= 1
                else:
                    j = -2
            
            if j == -1:
                flag = False

        return result

a = 1
b = 1
test = Solution()
print(test.combine(a,b))
    