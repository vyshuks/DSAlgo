"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/
"""

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n <= 1:
            return 0
        
        res = 0
        
        graph = collections.defaultdict(list)
        
        for idx, parent in enumerate(manager):
            graph[parent].append(idx)
            
        q = deque([(headID, informTime[headID])])
        
        while q:
            cur_emp, cur_time = q.popleft()
            
            res = max(res, cur_time)
            
            for report in graph[cur_emp]:
                q.append((report, cur_time + informTime[report]))
                
            
            
        return res
        