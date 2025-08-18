#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bb = float('inf') 
        bp = 0
        for x in prices:
            if x < bb: bb = x
            if x - bb > bp: bp = x - bb
        return bp
        
# @lc code=end

