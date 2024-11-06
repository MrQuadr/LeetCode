#
from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        
        while left <= right:
            if height[left] > left_max:
                left_max = height[left]
            if height[right] > right_max:
                right_max = height[right]
            
            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
                
        return water
            




a = [0,1,0,2,1,0,1,3,2,1,2,1]
a = [0,1,1,1,1,2,3,4,2,1,0]
test = Solution()
print(test.trap(a))