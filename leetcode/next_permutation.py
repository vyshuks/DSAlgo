"""
https://leetcode.com/problems/next-permutation/
"""
from typing import List

def next_permutation(nums: List) -> List:

    nums_len = len(nums)

    idx1  = idx2 = 0

    for i in range(nums_len-1, -1, -1):
        if nums[i-1] < nums[i]:
            idx1 = i-1
            break

    if idx1 >= 0:
        for i in range(nums_len-1, -1, -1):
            if nums[i] > nums[idx1]:
                idx2 = i
                break

    if idx1 >=0  and idx2 >=0:
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
        i = idx1+1
        j = nums_len-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
        
    else:
        i = 0
        j = nums_len-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
    return nums

    


print(next_permutation([1,3,2]))

    

