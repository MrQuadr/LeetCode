# 1829. Maximum XOR for Each Query -> https://leetcode.com/problems/maximum-xor-for-each-query/description/

class Solution:

    def __init__(self) -> None:
        pass

    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        maximum = (1 << maximumBit) - 1
        answer = [maximum := maximum ^ num for num in nums][::-1]
        return answer

if __name__ == "__main__":
    test = Solution()
    nums = [0,1,1,3]
    maximumBit = 2
    print(test.getMaximumXor(nums, maximumBit))

    nums = [2,3,4,7]
    maximumBit = 3
    print(test.getMaximumXor(nums, maximumBit))

    nums = [0,1,2,2,5,7]
    maximumBit = 3
    print(test.getMaximumXor(nums, maximumBit))
    