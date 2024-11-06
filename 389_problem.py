#
class Solution:

    def __init__(self) -> None:
        pass

    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if t.count(i) > s.count(i):
                return i
        return t[-1]
        # temp_str = s + t
        # temp_char = 0

        # for i in enumerate(temp_str):
        #     temp_char ^= ord(i[1])
        
        # return chr(temp_char)

a = 'cabd'
b = 'abecd'
test = Solution()
print(test.findTheDifference(a,b))
    