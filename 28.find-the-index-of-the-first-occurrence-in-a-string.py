#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def helper(i):
            if i + len(needle) > len(haystack):
                return -1
            
            if haystack[i:i+len(needle)] == needle:
                return i
            
            return helper(i + 1)
        
        return helper(0)

        
# @lc code=end

