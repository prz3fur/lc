#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        clean = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return clean == clean[::-1]
        
# @lc code=end

