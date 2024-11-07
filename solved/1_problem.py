# 1. Two Sum -> https://leetcode.com/problems/two-sum/description/

class Solution:
    def __init__(self) -> None:
        pass

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        temp_dict = {}
        for i, n in enumerate(nums):
            temp_value = target - n
            if temp_dict.get(n) is None:
                temp_dict[temp_value] = i
            else:
                return [temp_dict[n], i]
        return -1


if __name__ == "__main__":
    a = [3,2,4]
    b = 6
    test = Solution()
    print(test.twoSum(a, b))