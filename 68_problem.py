#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        print(words)
        temp = []
        finish = len(words) - 1
        start = 0
        space = 0
        limit = 0

        for j in words:
            limit += len(j)
            space += 1
            if limit + space >= maxWidth:
                print(j, limit+space)
                limit = len(j)
                start += space
                space = 1
            else:
                if start + space == finish:
                    print([j], limit+space)
        return temp


a = ["This", "is", "an", "example", "of", "text", "justification."]
b = 16
test = Solution()
print(test.fullJustify(a,b))
    