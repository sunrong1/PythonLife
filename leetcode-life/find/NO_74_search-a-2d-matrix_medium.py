from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False
    length = len(matrix)
    start = 0
    end = length - 1
    mid = (start + end) // 2
    is_find_list_pos = False
    while start <= end:
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            is_find_list_pos = True
            break
        elif target < matrix[mid][0]:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    print(mid)
    if not is_find_list_pos:
        return False
    l = 0
    r = len(matrix[mid]) - 1
    while l <= r:
        m = (l + r) // 2
        if matrix[mid][m] == target:
            return True
        elif target > matrix[mid][m]:
            l = m + 1
        else:
            r = m - 1
    return False


"""
第二次编写
变量写的更快速，随意，效率高；实际调试过程中，框架想清楚后，边界要想的更清楚些；
二分算法，写的更熟练
"""


def searchMatrix2(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False
    l = 0
    r = len(matrix) - 1
    rowIndex = 0
    while l <= r:
        mid = (l + r) // 2
        if matrix[mid][0] > target:
            r = mid - 1
        elif matrix[mid][0] <= target and matrix[mid][-1] >= target:
            rowIndex = mid
            break
        else:
            l = mid + 1
    if l > r:
        return False
    ll = 0
    rr = len(matrix[rowIndex]) - 1
    while ll <= rr:
        mid = (ll + rr) // 2
        if matrix[rowIndex][mid] > target:
            rr = mid - 1
        elif matrix[rowIndex][mid] < target:
            ll = mid + 1
        else:
            return True
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
matrix = [[1], [3]]
matrix = [[1, 3]]
print(searchMatrix2(matrix, 3))
