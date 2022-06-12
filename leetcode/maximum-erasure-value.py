"""
https://leetcode.com/problems/maximum-erasure-value/
"""
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i,j = 0,0
        result = 0
        output = 0
        
        L = len(nums)
        d = {}
        
        while j < L:
            if nums[j] in d:
                
                while i<j and i<=d[nums[j]]:
                    result-=nums[i]
                    i+=1
                    print(result)
                        
            d[nums[j]] = j
            result+= nums[j]
            output = max(output, result)
                 
            
            j+=1
            
        return output
