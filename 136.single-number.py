#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for x in nums:
            seen[x] = seen.get(x, 0) + 1
        for k, v in seen.items():
            if v != 2:
                return k


        
# @lc code=end

