#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer, righ_pointer = 0, len(height) - 1
        max_area = 0

        while left_pointer < righ_pointer:
            h = min(height[left_pointer], height[righ_pointer])
            w = righ_pointer - left_pointer
            max_area = max(max_area, h * w)

            if height[left_pointer] < height[righ_pointer]:
                left_pointer += 1
            else:
                righ_pointer -= 1

        return max_area

# @lc code=end

