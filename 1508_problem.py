#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = pow(10,9) + 7
        left -= 1
        k = 0

        for i in range(1, n):
            for j in range((n-i)):
                nums.append(nums[k+j]+nums[i+j])
            k += n + 1 - i
        
        nums.sort()
        return sum(nums[left:right]) % mod

a = [1,2,3,4]
n = 4
b = 1
c = 5
test = Solution()
print(test.rangeSum(a,n,b,c))
    