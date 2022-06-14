"""
https://leetcode.com/problems/maximum-alternating-subsequence-sum/
"""
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        oddsum, evensum = 0, 0
        
        for num in nums:
            oddsum, evensum = max(oddsum, evensum-num), max(evensum, oddsum+num)
        return evensum
        
        
#         memo = {}
        
#         def find_sum(index, type_of_indices, memo):
#             if index == len(nums):
#                 return 0
#             if (index, type_of_indices) in memo:
#                 return memo[(index, type_of_indices)]
            
#             current_val = nums[index] if type_of_indices else -nums[index]
#             memo[(index, type_of_indices)] = max(current_val + find_sum(index+1, not type_of_indices, memo), find_sum(index+1, type_of_indices, memo))
#             return memo[(index, type_of_indices)]
        
#         return find_sum(0, True, memo)
        
            
        
        