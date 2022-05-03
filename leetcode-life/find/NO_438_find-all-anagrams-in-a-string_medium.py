"""
查找类似的字符串
ord函数，返回ASCII的数值
"""
from typing import List

"""
方法1
首先暴力解法是两遍遍历可以解决，但是时间会很长，需要使用字典优化
需要充分利用窗口和滑动特性
1. 初始化need字典的个数
2. 初始化window字典的个数，后面只需修改个数即可
3. 开始索引遍历，遍历后，need字典和window字典，每个字符的个数相等的，即是需要的返回值，异位词
4. 窗口变动小，只需要修改改变字符的个数即可（这个是关键）
"""


def findAnagrams(s: str, p: str) -> List[int]:
    if not s:
        return []
    if len(s) < len(p):
        return []
    l = 0
    r = len(p) - 1
    need = {}
    # 初始化need字典的个数
    for pp in p:
        if pp in need:
            need[pp] = need.get(pp) + 1
        else:
            need[pp] = 1
    ret = []
    window = dict()
    # 初始化window的个数，后面只需修改个数即可
    for i in range(len(p)):
        if s[i] in window:
            window[s[i]] += 1
        else:
            window[s[i]] = 1
    # 开始索引遍历
    while r < len(s):
        same = True
        for i in need:
            if i not in window:
                same = False
                break
            if need[i] != window[i]:
                same = False
                break
        if same:
            ret.append(l)

        l += 1
        r += 1
        # 窗口变动小，只需要修改改变字符的个数即可
        if r <= len(s) - 1:
            window[s[l - 1]] -= 1
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1
    return ret


s = "abab"
p = "ab"

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))
