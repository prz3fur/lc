#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter()
        nums[:] = [x for x in nums if counter.update([x]) or counter[x] <= 2]
        k = len(nums)
        
        return k
# @lc code=end

