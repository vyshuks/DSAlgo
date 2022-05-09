"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        lookup = {
            "2": "abc", 
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = [""]
        
        for d in digits:
            temp = []
            for char in lookup[d]:
                for ch in result:
                    temp.append(ch+char)
            result = temp
            
        return result
        
        
        