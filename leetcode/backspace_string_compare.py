"""
https://leetcode.com/problems/backspace-string-compare/
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        pointerS = len(S)-1
        pointerT = len(T)-1
        skipS = skipT = 0
        while ((pointerS >= 0) or (pointerT >= 0)):

            while pointerS >= 0:
                if S[pointerS] == '#':
                    pointerS -= 1
                    skipS += 1
                elif skipS > 0:
                    skipS -= 1
                    pointerS -= 1
                else:
                    break

            while pointerT >= 0:
                if T[pointerT] == '#':
                    pointerT -= 1
                    skipT += 1
                elif skipT > 0:
                    skipT -= 1
                    pointerT -= 1
                else:
                    break

            if S[pointerS] != T[pointerT]:
                return False

            if (pointerS >= 0) != (pointerT >= 0):
                return False

            pointerS -= 1
            pointerT -= 1

        return True
