"""
https://leetcode.com/problems/stamping-the-sequence/
"""

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target_len = len(target)
        stamp_len = len(stamp)
        
        output = []
        
        move, max_move = 0, 10*target_len
        premove = 0
        
        def check_subseq(src, trg):
            works = False
            for i in range(stamp_len):
                if src[i] == trg[i]:
                    works=True
                elif src[i] == '?':
                    continue
                else:
                    return False
            return works
       
        ans_str = '?'*target_len
        while move < max_move:
            premove=move
            for i in range(target_len-stamp_len+1):
                if check_subseq(target[i: stamp_len+i], stamp):
                    move+=1
                    output.append(i)
                    target = target[:i]+'?'*stamp_len+target[stamp_len+i:]
                    if target == ans_str:
                        return reversed(output)
            if premove == move:
                return []
                    
        