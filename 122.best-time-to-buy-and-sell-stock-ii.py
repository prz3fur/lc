#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bb = float('inf') 
        tp = 0
        for x in prices:
            if x < bb: bb = x
            if x - bb > 0: tp, bb = tp + x - bb, float('inf')
            if x < bb: bb = x
        return tp
# @lc code=end

