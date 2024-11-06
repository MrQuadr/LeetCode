#

class Solution:
    
    def __init__(self) -> None:
        pass

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        str_out = [''] * numRows
        index = 0
        step = 1
        numRows -= 1

        for i in s:
            str_out[index] += i
            if not index:
                step = 1
            elif not index ^ numRows:
                step = -1
            index += step

        return ''.join(str_out)             

a = "PAYPALISHIRING"
test = Solution()
print(test.convert(a,3))

# def convert(self, s: str, numRows: int) -> str:
#         length_str = len(s)
#         max_space = (numRows - 1) << 1
#         list_space = [(i*" ") for i in range((max_space-1), 0, -2)]
#         list_space.append(list_space[0])
#         temp_str = ["" for i in range(numRows)]
#         str_out = ''

#         for i in range(numRows):
#             j = i
#             z = i << 1
#             y = i

#             while j < length_str:
#                 temp_str[i] += s[j] + list_space[y]

#                 y = numRows - 1 - y
#                 j += max_space

#                 if (z > 0) & (z < max_space):
#                     j -= z
#                     z = max_space - z
        
#         for i in temp_str:
#              str_out += i + '\n'
        
#         return str_out    