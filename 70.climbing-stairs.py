#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # just a Fibonacci:
        first, second = 1, 2
        for i in range(3, n + 1):
            first, second = second, first + second
        
        return second

        
# @lc code=end
