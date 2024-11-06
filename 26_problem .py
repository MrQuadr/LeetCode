#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0

        for i in nums:
            if nums[count] < i:
                count += 1
                nums[count] = i
        return (count + 1), nums[:(count + 1)]
        
a = [1,1,2]
test = Solution()
print(test.removeDuplicates(a))
    