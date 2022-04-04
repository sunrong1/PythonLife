from typing import List

"""
奇偶场景：
4个字符串：2 2分组

5个：2 + 1 +2  中间的不动
"""


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    length = len(s)
    for i in range(length // 2):
        temp = s[i]
        s[i] = s[length - 1 - i]
        s[length - 1 - i] = temp
    print(s)


s = ["sun", "rong"]
reverseString(s)
print(s)
