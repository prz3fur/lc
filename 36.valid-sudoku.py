#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]
        for i, line in enumerate(board):
            for j, x in enumerate(line):
                if x == ".":
                    continue
                rows[i].append(x)
                cols[j].append(x)
                squares[(i//3) * 3 + (j //3)].append(x)
        for row in rows:
            if len(set(row)) != len(row):
                return False
        for col in cols:
            if len(set(col)) != len(col):
                return False
        for square in squares:
            if len(set(square)) != len(square):
                return False
        
        return True


                

        
# @lc code=end

