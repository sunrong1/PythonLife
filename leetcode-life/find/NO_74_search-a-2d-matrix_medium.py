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

"""


def searchMatrix2(matrix: List[List[int]], target: int) -> bool:
    pass


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
print(searchMatrix(matrix, 3))
