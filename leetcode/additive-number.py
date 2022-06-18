"""
https://leetcode.com/problems/additive-number/
"""

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def check_res(n1,n2,s, found):
            if found and s=="":
                return True
            n3 = n1+n2
            n3_str = str(n3)
            idx = min(len(s), len(n3_str))
            
            if n3_str ==  s[:idx]:
                return check_res(n2,n3,s[idx:], True)
            return False
                
            
        
        N = len(num)
        for i in range(1, N-1):
            n1_str = num[:i]
            n1 = int(n1_str)
            if str(n1) != n1_str:
                break
            
            for j in range(i+1, N):
                n2_str = num[i: j]
                if (n2_str==""): break
                n2 = int(n2_str)
                if str(n2) != n2_str:
                    break
                
                found = check_res(n1,n2, num[j:], False)
                if found:
                    return True
        return False
                
        