#

class Solution:

    def __init__(self) -> None:
        pass
    
    def toLowerCase(self, s: str) -> str:
        # return s.lower()
        const = 0x20
        temp = ''

        for i in s:
            j = ord(i)
            if j > 0x40 and j < 0x5b:
                temp += chr(j^const)
            else:
                temp += i

        return temp


a = "LOVE&LY"
test = Solution()
print(test.toLowerCase(a))
    