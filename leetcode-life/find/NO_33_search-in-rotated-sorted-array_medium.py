from typing import List

"""
分段判断的二分查找

四种情况：操作较复杂，分两次二分查找

特例补充：
单升序数组，有可能
"""

"""
方法1：
两次二分
"""


def search(nums: List[int], target: int) -> int:
    length = len(nums)
    # 补充特例场景
    if length < 1:
        return -1
    if length == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    mid = length // 2
    start = 0
    end = length - 1
    # 寻找降序的第一个位置
    index = length - 1
    while start <= end:
        # 找到排序突变的位置
        if nums[mid] > nums[start]:
            if mid + 1 < length and nums[mid + 1] < nums[mid]:
                index = mid + 1
                break
            start = mid + 1
            mid = (start + end) // 2
        elif nums[mid] < nums[start]:
            if nums[mid - 1] > nums[mid]:
                index = mid
                break
            end = mid - 1
            mid = (start + end) // 2
        else:
            # mid 和start相等，说明数组最多还有两个元素
            if mid + 1 > length - 1:
                index = length - 1
            elif nums[mid] > nums[mid + 1]:
                index = mid + 1
            break

    # print("index", index)

    # if nums[index] > target or nums[index - 1] < target:
    #     return -1
    if nums[0] > target:
        start = index
        end = length - 1
    else:
        start = 0
        # 单升序场景
        if nums[index] > nums[0]:
            end = index
        else:
            end = index - 1
    mid = (start + end) // 2
    while start <= end:
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid
        mid = (start + end) // 2
    return -1


"""
算法设计2：
读懂题意，理解题意，抽象化，设计算法骨架，进行比较，选择最优，编写代码；

二分合并
本质是一个升序序列，分割成两个升序序列
搜索突变中，进行二分

[4, 6, 7,9,-2 0, 2]
是否再单升序列中：
    mid的位置可以根据和start大小的比较获得

target< mid: 目标值在序列的左半段
    target 和 start大小比较：
        <start 只可能再右升序列中
            
        >start 只可能再左升序列
    
    
target >mid：index 需要右移,target在序列的后半段
    可能是左边的后半段，也可能是右边的后半段
    # mid 再左升序中，
        target一定再左升序中，start变化
    # mid 在右升序中，可能更大的数在左升序中，需要进行判断在哪个升序序列中
        
mid ==target 
"""


def search1_1(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        # target值比较小，target在整体序列的左半段
        if target < nums[mid]:
            # target不在左升序序列，只可能再右升序列中
            if target < nums[start]:

                start = mid + 1
            # target在左升序中
            elif target > nums[start]:
                end = mid - 1
            else:
                return start
        elif target > nums[mid]:  # target 在序列的后半段
            # nums[end]是关键判断点
            # target 不在右升序中
            if target > nums[end]:
                # error : start 不能动
                # end 确认不了，start处也确定不了
                if nums[mid] > nums[start]:
                    start = mid + 1
                else:
                    end = end - 1
            # target 只在右升序中
            elif target < nums[end]:
                start = mid + 1
            else:
                return end
        else:
            return mid
    return -1

    # nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [4, 5, 6, 7, 8, 1, 2, 3]


"""
第二次编写
思路更清晰，但是还得得多练习2more
先思路阶梯模板，然后再填充特例，效率更高；
根据阶梯图，mid的位置进行判断
mid 的两边总有一个是有序的
mid左边有序，mid右边有序

"""


def search2(nums: List[int], target: int) -> int:
    length = len(nums)
    if length < 1:
        return -1
    l = 0
    r = length - 1

    while l <= r:
        mid = (l + r) // 2
        # target 较小
        if nums[mid] > target:
            # 左半部分有序
            if nums[mid] > nums[l]:
                # 在左半部分
                if nums[l] < target:
                    if nums[r] == target:
                        return r
                    r = mid - 1
                # 在右半部分
                elif nums[l] > target:
                    l = mid + 1
                else:
                    return l
            # 右半部分有序
            else:
                # 右半部分有序，target肯定在左边
                if nums[r] == target:
                    return r
                r = mid - 1
        # target值较大
        elif nums[mid] < target:
            # 左边有序，肯定在右边
            if nums[mid] > nums[l]:
                if nums[l] == target:
                    return l
                l = mid + 1
            # 右边有序
            else:
                # 在右半部分
                if nums[r] > target:
                    if nums[l] == target:
                        return l
                    l = mid + 1
                # 在左半不符
                elif nums[r] < target:
                    r = mid - 1
                else:
                    return r
        else:
            return mid
    return -1


nums = [5, 1, 2, 3, 4]
# nums = [1, 2, 3]
# nums = [6, 7, 8, 1, 2, 3, 4, 5]
# nums = [4, 5, 6, 7, 0, 1, 2]
nums = [1]
nums = [5, 1, 3]

# nums = [8, 1, 2, 3, 4, 5, 6, 7]
print(search2(nums, 5))
