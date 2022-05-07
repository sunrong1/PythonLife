"""
被包围的区域填充
"""
from typing import List

"""
方法1
深度优先搜索
1more
思路：所有最终会被标记为O的，都是和边缘O关联的O，其他的O都会被标记为X
四条边上的O，向里面进行延伸
递归停止条件：超出边界，不是O；
前进段：否者设置成A
后退段：无；

算法设计错误，思路错误，结果会总也不对；
"""


def solve(board: List[List[str]]) -> None:
    if not board:
        return
    row = len(board)
    col = len(board[0])

    def dfs(x, y):
        if not 0 <= x < row or not 0 <= y < col or board[x][y] != 'O':
            return
        board[x][y] = 'A'
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

    for i in range(row):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][col - 1] == 'O':
            dfs(i, col - 1)
    for j in range(col):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[row - 1][j] == 'O':
            dfs(row - 1, j)
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'A':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'
    return board


board = [["X"]]
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
# board = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
#          ["O", "X", "O", "X", "O", "X"]]
board = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], ["X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"],
         ["X", "X", "O", "X", "O"]]

board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
print(solve(board))
