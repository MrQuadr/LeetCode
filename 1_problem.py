list

class Solution:
    def __init__(self) -> None:
        pass

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        temp_dict = {}
        for i, n in enumerate(nums):
            temp_value = target - n
            if temp_dict.get(n) != None:
                return [temp_dict[n], i]
            else:
                temp_dict[temp_value] = i
        return "Что-то пошло не так"


a = [3,2,4]
b = 6
test = Solution()
print(test.twoSum(a, b))