"""
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
"""

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        del_sum = 0
        no_del_sum = arr[0]
        answer = arr[0]
        
        for i in range(1, n):
            del_sum = max(del_sum+arr[i], no_del_sum )
            no_del_sum = max(arr[i], no_del_sum+arr[i])
            answer = max(answer, del_sum, no_del_sum)
            
        return answer
        