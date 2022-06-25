"""
https://leetcode.com/problems/create-sorted-array-through-instructions/
"""

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mx = max(instructions)
        arr = [0]*(mx+1)
        
        def update(x):
            while x <= mx:
                arr[x]+=1
                x += x & -x
        
        def get(x):
            res = 0
            while x > 0:
                res+=arr[x]
                x-= x & -x
            return res
        
        res = 0
        
        for i, num in enumerate(instructions):
            res += min(get(num-1), i - get(num))
            update(instructions[i])
        
        print(arr)
        mod = 10**9 + 7
        return res % mod