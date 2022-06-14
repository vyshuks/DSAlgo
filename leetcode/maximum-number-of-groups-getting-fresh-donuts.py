"""
https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/
"""
class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        l = [g % batchSize for g in groups]
        g = [0]*batchSize
        for i in l:
            g[i] += 1
            
        # count = Counter(l)
        # g = [count[i] for i in range(batchSize)]
          
        self.memo = {}
        def dp(sm, t):
            key = (sm, tuple(t))
            if key in self.memo:
                return self.memo[key]
            if max(t) == 0:
                return 0
            ans, arr = 0, list(t)
            for k in range(batchSize):
                if arr[k] == 0:
                    continue
                arr[k] -= 1
                ans = max(ans, dp((sm + k) % batchSize, arr))
                arr[k] += 1
            self.memo[key] = ans + (sm == 0)
            return ans + (sm == 0)

        return dp(0, g)