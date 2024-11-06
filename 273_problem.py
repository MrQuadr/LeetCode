#

class Solution:

    def __init__(self) -> None:
        pass

    def numberToWords(self, num: int) -> str:
        numbers = { 0: ["Zero"," One"," Two"," Three"," Four"," Five"," Six"," Seven"," Eight"," Nine"],
                   1:[" Ten"," Eleven"," Twelve"," Thirteen"," Fourteen"," Fifteen"," Sixteen"," Seventeen"," Eighteen"," Nineteen"],
                   2:[" Twenty"],
                   3:[" Thirty"],
                   4:[" Forty"],
                   5:[" Fifty"],
                   6:[" Sixty"],
                   7:[" Seventy"],
                   8:[" Eighty"],
                   9:[" Ninety"]}
        _100 = " Hundred"
        exp = {0: "", 1: " Thousand", 2: " Million", 3: " Billion"}
        out_str = ""
        ind = 0

        if num == 0:
            return numbers[0][0]

        while num > 0:
            x = (num % 1000) // 100
            y = (num % 100) // 10
            z = num % 10
            num //= 1000

            temp = ""

            if x > 0:
                temp += numbers[0][x] + _100
            
            if y > 1:
                temp += numbers[y][0]
                if z > 0:
                    temp += numbers[0][z]
            else:
                if z != 0 or y != 0:
                    temp += numbers[y][z]
            
            if x != 0 or y != 0 or z != 0:
                out_str = temp + exp[ind] + out_str

            ind += 1
            
        
        return out_str[1:]

        
a = 1000001
test = Solution()
print(test.numberToWords(a))
    