#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n
        
        while j >= 0:
            k -= 1
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
        
        return nums1

a = [1,6,7,0,0,0]
c = 3
b = [2,5,6]
d = 3
test = Solution()
print(test.merge(a,c,b,d))
    