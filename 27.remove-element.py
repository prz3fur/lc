#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        k = len(nums)
        return k
        
# @lc code=end

