#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
    
        # collect vowels
        found = [c for c in s if c in vowels][::-1]

        result = []
        for c in s:
            if c in vowels:
                result.append(found.pop(0))  # replace with reversed vowel
            else:
                result.append(c)
        return "".join(result)
        
# @lc code=end

