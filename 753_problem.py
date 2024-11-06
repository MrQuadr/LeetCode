#

class Solution:

    def __init__(self) -> None:
        pass

    def crackSafe(self, n: int, k: int) -> str:

        def dfs(prv, res, res_l):
            if len(res) == trg_l:     # reached target length
                res_arr.append(res)
                return

            prv = prv[1:]             # remove first number
            for i in map(str, range(k)):        # convert integer to string
                
                cur = prv + i  
                if cur in visited:   continue   # already have current password -> skip

                visited.add(cur)      
                dfs(cur, res + i, res_l + 1)    # try to find next password
                visited.remove(cur)   # this try was unsuccessful -> remove current password from set 

                if res_arr:   return  # interruption: find solution -> interrupt



        res_arr = []
        start_p = '0' * n             # initial password '0..0'
        visited = set([start_p])      
        trg_l   = k ** n + (n - 1)    # (n - 1) - because there is no cycle
        
        dfs(start_p, start_p, n)      # previous password, solution, current length of solution 

        return f'{len(res_arr[0])}\t--->\t{res_arr[0]}'

a = 8
b = 11
test = Solution()
for i in range(1, b):
    for j in range(1, a):
        print((j, i), "\t--->\t", test.crackSafe(j, i))
    