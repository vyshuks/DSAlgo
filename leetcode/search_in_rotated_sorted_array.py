"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List

def search(self, arr: List[int], target: int) -> int:
    if arr is None or not arr:
        return -1
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = start + (end-start) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] >= arr[start]:
            if arr[start] <= target < arr[mid]:
                end = mid-1
            else:
                start = mid+1
            
        else:
            if arr[mid] < target <= arr[end]:
                start = mid+1
            else:
                end = mid-1
        
    return -1
            