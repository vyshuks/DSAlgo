"""
https://leetcode.com/problems/permutation-sequence/
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        factorial = math.factorial(n)
        index = k-1
        output = []
        while nums:
            factorial = factorial//len(nums)
            pos = index//factorial
            output.append(nums.pop(pos))
            index = index%factorial
        return "".join(output)