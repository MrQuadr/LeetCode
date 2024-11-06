#

class Solution:

    def __init__(self) -> None:
        pass

    def mergeAlternately(self, word1: str, word2: str) -> str:
        k = max(len(word1),len(word2))
        temp_str = [''] * k

        for i,j in enumerate(word1):
            temp_str[i] = j
        for i,j in enumerate(word2):
            temp_str[i] += j
            
        return ''.join(temp_str)


a = 'abcd'
b = 'pq'
test = Solution()
print(test.mergeAlternately(a,b))