#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracking = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in tracking:
                return [tracking[complement], i]
            tracking[num] = i
        
# @lc code=end

