#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        flag = 0
        for i in enumerate(arr):
            if i[1] & 1:
                flag += 1
                if flag == 3:
                    return True
            else:
                flag = 0
            
        return False


a = [1,2,34,3,4,5,12,7,23]
# a = [2,6,4,1]
# a = [1,1,1]
test = Solution()
print(test.threeConsecutiveOdds(a))

    # def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    #     i = 0
    #     j = len(arr) - 2

    #     while i < j:
    #         if arr[i] & 1:
    #             if arr[i+1] & 1:
    #                 if arr[i+2] & 1:
    #                     return True
    #                 else:
    #                     i += 3
    #             else:
    #                 i += 2
    #         else:
    #             i += 1   
    #     return False