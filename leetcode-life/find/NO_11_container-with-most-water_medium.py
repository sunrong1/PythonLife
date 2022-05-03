"""
盛最多水的容器
实际上，这个是一个证明题；证明走的路线是对的

area = min(h(l),h(r)) * (r-l)
"""

from typing import List


def maxArea(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    area = 0
    while l < r:
        area = max(area, min(height[l], height[r]) * (r - l))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return area


num = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(num))
