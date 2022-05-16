from typing import List

"""
组合综合

方法1

"""


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    ret = []
    if not candidates:
        return ret
    candidates.sort()
    