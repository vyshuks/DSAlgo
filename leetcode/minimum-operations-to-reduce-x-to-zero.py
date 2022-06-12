"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        max_len = 0
        i,j = 0,0
        L = len(nums)
        total = 0
        total_array_sum = sum(nums)
        result_sum = total_array_sum-x
        found = False
        
        while j < L:
            total+= nums[j]
            
            while i<=j and total > result_sum:
                total-=nums[i]
                i+=1
            
            
            if total == result_sum:
                max_len = max(max_len, j-i+1)
                found = True
                
            j+=1
            
            
                
                
        return L - max_len if found else -1
            
        
    
    
        
        
            
        
        
        