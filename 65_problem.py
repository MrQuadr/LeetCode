#

class Solution:

    def __init__(self) -> None:
        pass

    def isNumber(self, s: str) -> bool:
        signs = ['+-', '.', 'eE', '+-']
        index = 0
        flag = False
        digit = False
        temp = 0

        for char in s:
            if char.isdigit():
                flag = True
                digit = True
            else:
                temp = index
                while (index < 4) and (char not in signs[index]):
                    index += 1
                    if index == 4:
                        return False
                    
                if index == 0:
                    if flag:
                        return False
                    flag = False
                elif index == 1:
                    flag = True
                elif index == 2:
                    if not flag:
                        return False
                    if not digit:
                        return False
                    flag = False
                    digit = False
                elif index == 3:
                    if flag or (temp == 1):
                        return False
                    flag = False
                else:
                    return False
                
                index += 1
        if digit:
            return True
        else:
            return False






a = ["0", "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", '46.e3', "+3.e04116", "32.e-80123", ".1", "0.8", "-1.", "-01", ".0e7","-.3e6", "1.38354e+8", ".703e+4144", "-.7e+0435", "3.", "+1.3e-7"]
b = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53","6+1", ".-4", "92e1740e91", ".", ".e1", "7j1", "G76", "3.5e+3.5e+3.5"]
test = Solution()
for i in a:
    print(test.isNumber(i), "\t--->\t", i)

for i in b:
    print(test.isNumber(i), "\t--->\t", i)
