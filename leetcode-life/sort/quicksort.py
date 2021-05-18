"""

快速排序，采用分治的思想进行排序
分割排序，双指针法排序
"""


def partition(arr, low, high):
    """
    方法1：双边循环方法
    :param arr:
    :param low:
    :param high:
    :return:
    """
    # 选择基准数进行比较，基准数的选择比较任意，可以选择最头的，也可以是尾部，也可以中间
    pivot = arr[low]
    left = low
    right = high
    while left < right:
        # 双循环的位置对结果也有很大的影响，右指针先走，保证最后指针的位置是小于pivot的
        while left < right and arr[right] > pivot:
            right -= 1
        while left < right and arr[left] <= pivot:
            left += 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low] = arr[left]
    arr[left] = pivot
    print(arr)
    return left


def quicksort_v1(arr, low, high):
    """
    递归过程，partition
    :param arr:
    :param low:
    :param high:
    :return:
    """
    if low < high:
        p = partition(arr, low, high)
        print("p:", p)
        quicksort_v1(arr, low, p - 1)
        quicksort_v1(arr, p + 1, high)


arr = [2, 3, 1, 7, 1]
# > 1 1 7 3
# >
quicksort_v1(arr, 0, len(arr) - 1)
print(arr)
