"""
https://leetcode.com/problems/3sum-with-multiplicity/
"""

from typing import List

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count  = 0
        counter = {}
        MOD = 10**9 + 7
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        
        
        for i in counter:
            for j in counter:
                
                k = target - i - j
               
                if k not in counter:
                    continue
                    
                
                if i < j< k:
                    count += (counter[i] * counter[j] * counter[k])
                    
                elif i==j and j != k:
                    count += (counter[i] * (counter[j]-1)//2 * counter[k])
                    
                elif i == j== k:
                    count += (counter[i] * (counter[j]-1) * (counter[k]-2))//6
                   

                
                
        count%=MOD    
        return count