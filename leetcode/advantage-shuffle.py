"""
https://leetcode.com/problems/advantage-shuffle/
"""

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2_list = sorted([(v,i) for i,v in enumerate(nums2)])
        L =len(nums1)
        
        l,r = 0, L-1
        output = [-1]*L
        
        for i in range(L-1,-1,-1):
            if nums1[r] > nums2_list[i][0]:
                output[nums2_list[i][1]] = nums1[r]
                r-=1
            else:
                output[nums2_list[i][1]] = nums1[l]
                l+=1
        return output
                
                
        