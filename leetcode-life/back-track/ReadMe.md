# 回溯算法 backtrack - true

方法本质是抽象成一个树形结构，核心就是爬树的三要素：
- 路径
- 路径选择
- 停止条件

因为到了终止条件，往回迭代，所以回溯肯定包含递归（理解的递归，算法的理解感觉大幅提升一个档次）。

典型代码结构：
 ```python
def backtrack(param):
    if condition:
        res.append(path[:])
        return 
    for i in range(FirstLayerList):
        path.append()
        backtrack(param+1)
        path.pop()
backtrack()
 ```
## 组合问题 
典型题目：77，

组合没有顺序，排列有顺序
## 排列问题
Leetcide 78，90

## 切割问题
Leetcode 131，字符串切割

## 排列问题
Leetcode 491

## 排列问题
典型题目



## 参考
- B站 代码随想录
- 我的小沐助手