"""
https://leetcode.com/problems/sort-integers-by-the-power-value/
"""

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.memo = {}
        
        def find_power(num):
            
            if num==1:
                return 0
            
            if num in self.memo:
                return self.memo[num]
            if num %2==0:
                self.memo[num] = 1+find_power(num//2)
            else:
                self.memo[num] = 1+find_power(num*3+1)
            return self.memo[num]
            
        
        res=[]
        
        for i in range(lo,hi+1):
            res.append((find_power(i), i))
        
        res.sort(key=lambda x: (x[0],x[1]))
        
        return res[k-1][1]
        