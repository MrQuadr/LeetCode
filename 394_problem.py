#

class Solution:

    def __init__(self) -> None:
        pass

    def decodeString(self, s: str) -> str:
        temp = ""
        i, k, x = 0, 0, 0
        flag = True

        for j, z in enumerate(s):
            if z == '[':
                if k == 0:
                    i = j + 1
                    flag = False
                k += 1  
            elif z == ']':
                k -= 1
                if k == 0:
                    temp += self.decodeString(s[i:j]) * x
                    flag = True
                    x = 0
            elif z.isdigit():
                if flag:
                    x *= 10
                    x += int(z)
            else:
                if flag:
                    temp += z
                
        return temp

a = "3[a2[c]]"
test = Solution()
print(test.decodeString(a))
    