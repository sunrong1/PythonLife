from typing import List

"""
寻找区间的交集
"""


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    l = 0
    r = 0
    ret = []
    for l in firstList:
        r = 0
        while r < len(secondList):
            if secondList[r][0] > l[-1]:
                break
            a = max(l[0], secondList[r][0])
            b = min(l[1], secondList[r][1])
            if a <= b:
                ret.append([a, b])
                r += 1
            else:
                r += 1
    return ret


"""
方法2：
寻找规律，保持原有状态前进，但是不是一般的规律，看了官方解答，知道可以更一般化的解答
"""


def intervalIntersection0(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    r = 0
    if not firstList or not secondList:
        return []
    ret = []
    for l in firstList:
        hasjoin = False
        while r < len(secondList):
            if secondList[r][0] > l[-1]:
                # 如果有交集，回到上次有交集的地方
                if hasjoin:
                    r -= 1
                    hasjoin = False
                break
            a = max(l[0], secondList[r][0])
            b = min(l[1], secondList[r][1])
            if a <= b:
                ret.append([a, b])
                hasjoin = True
            r += 1
        if hasjoin:
            r -= 1
    return ret


firstList = [[1, 7], [8, 11]]
secondList = [[3, 10]]

firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
# firstList = [[0, 2], [5, 10]]
# secondList = [[1, 5], [8, 12]]

# firstList = [[0, 5], [12, 14], [15, 18]]
# secondList = [[11, 15], [18, 19]]
#
# firstList = [[4, 6], [7, 8], [10, 17]]
# secondList = [[5, 10]]
print(intervalIntersection0(firstList, secondList))
