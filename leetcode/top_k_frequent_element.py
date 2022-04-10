"""
https://leetcode.com/problems/top-k-frequent-elements/
"""

from typing import List
import heapq

def top_k_frequent_element(nums: List[int], k: int) -> List[int]:
    counter = {}

    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    data = []
    for num in counter:
        data.append((counter[num], num))
    heapq.heapify(data)
    
    while len(data) > k:
        heapq.heappop(data)
    result = []
    for d in data:
        result.append(d[1])

    return result

print(top_k_frequent_element([1,1,1,1, 2,2,2,3,4,4,4,4], 2))

