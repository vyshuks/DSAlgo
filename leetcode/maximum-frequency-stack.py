"""
https://leetcode.com/problems/maximum-frequency-stack/
"""
class FreqStack:

    def __init__(self):
        self.c = Counter()
        self.stack = defaultdict(list)
        self.maxfreq=0
        

    def push(self, val: int) -> None:
        self.c[val]+=1
        f = self.c[val]
        self.maxfreq = max(self.maxfreq, f)
        self.stack[f].append(val)
        

    def pop(self) -> int:
        cand = self.stack[self.maxfreq].pop()
        self.c[cand]-=1
        if not self.stack[self.maxfreq]:
            self.maxfreq-=1
        return cand
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()