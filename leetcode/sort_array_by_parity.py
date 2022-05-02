"""
https://leetcode.com/problems/sort-array-by-parity/
"""


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
#         e = []
#         o = []
        
#         for num in A:
#             if num%2 == 0:
#                 e.append(num)
#             else:
#                 o.append(num)
        
#         return [*e, *o]
        i , j = 0, len(A)-1
        while i < j:
            mod1 = A[i]%2
            mod2 = A[j]%2
            
            if mod1 > mod2:
                A[i],A[j] = A[j], A[i]
            
            if mod1==0:
                i+=1
            if mod2==1:
                j-=1
        return A