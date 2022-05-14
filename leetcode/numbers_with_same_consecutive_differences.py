"""
https://leetcode.com/problems/numbers-with-same-consecutive-differences/
"""

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        result = []
        
        def dfs(n, num):
            if n==0:
                result.append(num)
                return
                
            tail_digit = num%10
            next_digits = set([tail_digit+K, tail_digit-K])
            
            
            for next_digit in next_digits:
                if 0<= next_digit < 10:
                    new_num = num*10 + next_digit
                    dfs(n-1, new_num)
            
        for num in range(1,10):
            dfs(N-1, num)
            
        return result
            
        