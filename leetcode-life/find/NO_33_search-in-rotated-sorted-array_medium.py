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


def search2(nums: List[int], target: int) -> int:
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


nums = [5, 1, 2, 3, 4]
# nums = [1, 2, 3]
# nums = [6, 7, 8, 1, 2, 3, 4, 5]
# nums =[]
print(search2(nums, 1))
