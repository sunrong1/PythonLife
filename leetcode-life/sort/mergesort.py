"""
mergesort 归并排序
外部排序
"""


def merge_sort(arr, l, r):
    if l >= r:
        return
    mid = (r - l) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    int
    p1 = l
