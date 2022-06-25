"""
https://leetcode.com/problems/kth-smallest-instructions/
"""

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
               
        total_h, total_v = destination[1], destination[0]
        
                
        if k==1:
            return "H"*total_h + "V"*total_v
        
        ans = ""
        
        
        
        for i in range(total_h+total_v):
            
            c = comb(total_v+total_h-1, total_v)
            
            if k <= c:
                ans += 'H'
                total_h-=1
            else:
                ans+= 'V'
                k-=c
                total_v-=1
        return ans
            
            
                
        