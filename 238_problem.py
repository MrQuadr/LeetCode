#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        temp = [1] * length
        pref, post = 1, 1
        for i in range(length):
            temp[i] *= pref
            pref *= nums[i]
            temp[length-i-1] *= post
            post *= nums[length-i-1]
        return temp

a = [1,2,3,4]
test = Solution()
print(test.productExceptSelf(a))
    