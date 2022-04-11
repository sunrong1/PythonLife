from typing import List

"""
回溯算法
递归设计：
按照树展开，看括号的个数，左括号的优先级最高，要先加左括号

边界条件：左右括号的个数满足了2n时，递归结束。

"""


def generateParenthesis(n: int) -> List[str]:
    result = []

    def track(r: List, left, right):
        #
        if len(r) == 2 * n:
            result.append(''.join(r))
        # 先迭代进行左括号的
        if left < n:
            # 递归前进,加上左括号
            r.append('(')
            track(r, left + 1, right)
            # 递归回退时，弹出递归完成的
            r.pop()
        # 再迭代又括号的
        if right < left:
            r.append(')')
            track(r, left, right + 1)
            r.pop()

    track([], 0, 0)
    return result


print(generateParenthesis(11))
