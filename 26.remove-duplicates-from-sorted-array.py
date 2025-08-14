#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        nums[:] = [x for x in nums if not (x in seen or seen.add(x))]
        k = len(nums)
        
# @lc code=end

