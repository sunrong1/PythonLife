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


# print(generateParenthesis(11))

"""
第二次编写
题意理解：n=3 就是6个括号，三个左，三个右
递归设计：

递归停止条件：不符合条件的返回（右括号>左括号的数量），括号用完停止
前进段：括号用完的，加到结果集中
后退段：无

"""


def generateParenthesis2(n: int) -> List[str]:
    ret = []
    if n < 1:
        return ret
    p = ['('] * n + [')'] * n

    # 第一个循环 ( ( ) )
    # 第二个循环：( ) )
    def dfs(s, tmp: List):
        for i in range(s, n * 2):
            t = tmp + [p[i]]
            print(t)
            if t.count(')') > t.count('('):
                return
            if i == 2 * n - 1:
                ret.append(''.join(t))
                return
            dfs(i + 1, tmp + [p[i]])

    dfs(0, [])
    return ret


print(generateParenthesis2(2))
