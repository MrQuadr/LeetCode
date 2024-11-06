#

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def kthDistinct(self, arr: List[str], k: int) -> str:
        temp = {}
        for i in arr:
            if temp.get(i) == None:
                temp[i] = True
            else:
                temp[i] = False
        
        for j in temp.keys():
            if temp[j]:
                k -= 1
            if k == 0:
                return j

        return ""

a = ["l","eq","mqqlg","a","ydv","b","nkzot","dyzv","aiuuy","y","brn","fq","oaqkd","qwi","zd","lp","lnglw","kwb","oje","p","iq","w","hphk","guemh","ao","euu","q","jlbd","hj","zjzr","zanu","sp","bm","py","oe","ydsoj","taf","owlsv","fvp","yaubc","fh","rg","aa","tkb","r","pkuru","dt","rq","df","k","c","g","wj","wo","gqaa","d","m","izg","ml","by","vm","ad","hhzt","qexy","t","ftfh","vsmdo","fy","bc","n","d"]
k = 40
a = ["d","b","c","b","c","a"]
k = 2
test = Solution()
print(test.kthDistinct(a,k))
    