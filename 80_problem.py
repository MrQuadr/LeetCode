#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        flag = False

        if len(nums) == 0: return 0

        for j in nums[1:]:
            if nums[i] == j and flag:
                pass
            else:
                flag = True if nums[i] == j else False
                i += 1
                nums[i] = j
                
                
        
        return i+1, nums[:(i+1)]

                
        
a = [0,0,1,1,1,1,2,3,3]
test = Solution()
print(test.removeDuplicates(a))
    