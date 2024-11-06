#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[j] != val:
                if nums[i] == val:
                    nums[i] = nums[j]
                    j -= 1
                i += 1
            else:
                j -= 1
        
        if j == i and nums[0] != val and nums[i] != val:
            i += 1
        
        return i, nums[:i]
                
        
a = [2,2,2,3,2,2,3]
b = 2
test = Solution()
print(test.removeElement(a,b))
    