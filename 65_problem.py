#

class Solution:

    def __init__(self) -> None:
        pass

    def isNumber(self, s: str) -> bool:
        combination_form = [0x4, 0x12, 0x14, 0x18, 0x48, 0x4c, 0x52, 0x58, 0x12c, 0x134, 0x148, 0x14c, 0x18c, 0x48c, 0x4b4, 0x52c, 0x534, 0x58c, 0x634, 0x1234, 0x148c, 0x1634, 0x5234]
        temp_form = 0x1
        flag = True
        
        for i in s:
            x = ord(i)
            if 0x2f < x < 0x40:
                if flag:
                    temp_form <<= 2
                    temp_form += 0x0
                    flag = False
            elif x == 0x2b or x == 0x2d:
                temp_form <<= 2
                temp_form += 0x1
                flag = True
            elif x == 0x2e:
                temp_form <<= 2
                temp_form += 0x2
                flag = True
            elif x == 0x45 or x == 0x65:
                temp_form <<= 2
                temp_form += 0x3
                flag = True
            else:
                return False
        if temp_form in combination_form:
            return True
        else:
            return False



a = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", '46.e3', "+3.e04116", "32.e-80123", ".1", "0.8", "-1.", "-01", ".0e7","-.3e6", "1.38354e+8", ".703e+4144", "-.7e+0435", "+1.3e-7"]
b = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53","6+1", ".-4", "92e1740e91"]
test = Solution()
for i in a:
    print(test.isNumber(i), "\t--->\t", i)

for i in b:
    print(test.isNumber(i), "\t--->\t", i)


# number = {0x0: lambda x: True if (0x2f < x < 0x40) else False,
#                   0x1: lambda x: True if (x == 0x2b or x == 0x2d) else False,
#                   0x2: lambda x: True if (x == 0x2e) else False,
#                   0x3: lambda x: True if (x == 0x45 or x == 0x65) else False}
#         combination_form = [0x4, 0x12, 0x14, 0x18, 0x48, 0x4c, 0x52, 0x58, 0x12c, 0x134, 0x148, 0x14c, 0x18c, 0x48c, 0x4b4, 0x52c, 0x534, 0x58c, 0x634, 0x1234, 0x148c, 0x1634, 0x5234]
#         temp_form = 0x1
#         flag = True
        
#         for i in s:
#             if number[0x0](ord(i)):
#                 if flag:
#                     temp_form <<= 2
#                     temp_form += 0x0
#                     flag = False
#             elif number[0x1](ord(i)):
#                 temp_form <<= 2
#                 temp_form += 0x1
#                 flag = True
#             elif number[0x2](ord(i)):
#                 temp_form <<= 2
#                 temp_form += 0x2
#                 flag = True
#             elif number[0x3](ord(i)):
#                 temp_form <<= 2
#                 temp_form += 0x3
#                 flag = True
#             else:
#                 return False
#         if temp_form in combination_form:
#             return True
#         else:
#             return False

# number = {0x0: '0123456789', 0x1: '+-', 0x2: '.', 0x3: 'Ee'}
#         combination_form = [0x4, 0x12, 0x14, 0x18, 0x48, 0x4c, 0x52, 0x58, 0x12c, 0x134, 0x148, 0x14c, 0x18c, 0x48c, 0x4b4, 0x52c, 0x534, 0x58c, 0x634, 0x1234, 0x148c, 0x1634, 0x5234]
#         temp_form = 0x1
#         flag = True
        
#         for i in s:
#             if i in number[0x0]:
#                 if flag:
#                     temp_form <<= 2
#                     temp_form += 0x0
#                     flag = False
#             elif i in number[0x1]:
#                 temp_form <<= 2
#                 temp_form += 0x1
#                 flag = True
#             elif i in number[0x2]:
#                 temp_form <<= 2
#                 temp_form += 0x2
#                 flag = True
#             elif i in number[0x3]:
#                 temp_form <<= 2
#                 temp_form += 0x3
#                 flag = True
#             else:
#                 return False
#         if temp_form in combination_form:
#             return True
#         else:
#             return False