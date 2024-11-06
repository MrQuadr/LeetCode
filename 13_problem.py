#

class Solution:

    def __init__(self) -> None:
        pass

    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        value = d[s[0]]

        for i, j in enumerate(s[1:]):
            if d[s[i]] >= d[j]:
                value += d[j]
            else:
                value += d[j]
                index = 0

                while d[s[i-index]] < d[j] and index <= i:
                    value -= 2*d[s[i-index]]
                    index += 1

        return value


a = "MCXCIV"
test = Solution()
print(test.romanToInt(a))
    