#

class Solution:

    def __init__(self) -> None:
        pass

    def calculate(self, s: str) -> int:
        cur = res = 0
        stack = []
        sign = 1 #1 -> +1

        for char in s:
            if char.isdigit():
                cur = cur*10+int(char)
            elif char in ["+", "-"]:
                res += sign*cur

                sign = 1 if char=="+" else -1
                cur = 0
            elif char == "(":
                stack.extend([res, sign])
                sign = 1
                res = 0
            elif char == ")":
                res += sign*cur
                res *= stack.pop()
                res += stack.pop()
                cur = 0
            else:
                continue
        
        return res + sign*cur
        # znak, i, k, x, y = 1, 0, 0, 0, 0
        # flag = True

        # for j, z in enumerate(s):
            
        #     if z == '(':
        #         if k == 0:
        #             i = j + 1
        #             flag = False
        #         k += 1  
        #     elif z == ')':
        #         k -= 1
        #         if k == 0:
        #             flag = True
        #             x += self.calculate(s[i:j]) * znak
        #             y = 0
        #     elif z.isdigit():
        #         if flag:
        #             y *= 10
        #             y += int(z)
        #     else:
        #         if flag:
        #             x += znak * y
        #             y = 0
        #             if z == "+":
        #                 znak = 1
        #             if z == "-":
        #                 znak = -1
        # x += y * znak   
        # return x

a = "(1+(4+5+2)-3)+(6+8)"
test = Solution()
print(test.calculate(a))
    