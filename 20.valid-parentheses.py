#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        valid_pairs = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in ("({["):
                seen.append(char)
            elif char in (")}]"):
                if not seen or char != valid_pairs[seen[-1]]:
                    return False
                seen.pop()
        return not seen
# @lc code=end

