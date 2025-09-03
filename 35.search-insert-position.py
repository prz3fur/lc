#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for x in nums:
            if x == target:
                return index
            elif x > target:
                return index
            index += 1
        return len(nums)

            
        
# @lc code=end

