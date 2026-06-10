from typing import List

"""
回溯法
n个棋子放到N*N的棋盘上
：我的突破：实际程序还是串行执行的，没有并行执行
"""

class Solution:
      # row 行，col列
    def posRight(self, row,col,m):
        n = len(m[0])
        # 遍历前面的列有没有
        for r in range(row):
            if m[r][col] == "Q":
                return False
        # 对角线上
        i = row -1
        j = col -1
        while i >= 0 and j>=0:
            if m[i][j] == "Q":
                return 
            i = i - 1 
            j = j -1
        i = row -1
        j = col + 1
        while i >= 0 and j< n:

            if m[i][j] == "Q":
                return False
            i = i - 1 
            j = j + 1
        return True
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 路径是n个，横竖上不能包含棋子
        # 可选列表：n个里面选择一个位置放置棋子
        path =[]
        ret =[]
        matrix = [["." for _ in range(n)] for _ in range(n)]
        def backtrack(row):
            if row == n:
                ret.append(["".join(line) for line in matrix])
            # q 分别放置不同的位置上
            for i in range(n):
                if not self.posRight(row,i,matrix):
                    continue
                matrix[row][i] ="Q"
                backtrack(row+1)
                matrix[row][i] = "."
        
        backtrack(0)
        return ret
                         

s = Solution()
print(s.solveNQueens(4))
