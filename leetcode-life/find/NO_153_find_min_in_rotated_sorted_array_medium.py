from typing import List

"""
旋转后的最小值
旋转特性：两个升序序列，左大右小
旋转判断： 首位大小比较
情况判断：
1. 空数组
2. 未旋转的数组，直接访问nums[0]
3. 旋转的数组：
    寻找降序的起始位置
    [4,5,6,7,0,1,2]
    start <mid and mid >end 说明mid在左边，start = mid+1
    mid < start and < end ，mid 在右序列，end = mid -1
    m
    
"""


def findMin(nums: List[int]) -> int:
    if not nums:
        return -1
    length = len(nums)
    if nums[length - 1] >= nums[0]:
        return nums[0]
    l = 0
    r = length - 1
    mid = (l + r) // 2
    while l <= r:
        # 非单升序列的两个场景
        if nums[mid] > nums[l] and nums[mid] > nums[r]:
            l = mid + 1
        elif nums[mid] < nums[l] and nums[mid] < nums[r]:
            # 判断，避免漏掉右边的最小值
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            r = mid - 1
        # 单升序列场景 + 特殊相等场景
        elif nums[mid] == nums[l] and nums[mid] >= nums[r]:
            return nums[r]
        else:
            # nums[l] < nums[mid] < nums[r]:
            return nums[l]
        mid = (l + r) // 2


"""
第二次编写
思路更清晰，编程效率更高；
不过度考虑边界模式；边界条件更一般化处理
边界一般性处理：防止最小值出现在边界上，修改之前进行边界的判断
"""


def findMin2(nums: List[int]) -> int:
    if not nums:
        return -1
    l = 0
    r = len(nums) - 1
    min = nums[0]
    while l <= r:
        mid = (l + r) // 2
        # 左边有序
        if nums[mid] >= nums[l]:
            if nums[l] < min:
                min = nums[l]
            l = mid + 1
        else:
            if nums[r] < min:
                min = nums[mid]
            r = mid - 1
    return min


nums = [4, 5, 6, 7, 0, 1, 2]
nums = [2, 1]
nums = [3, 4, 5, 1, 2]
nums = [3, 1, 2]
nums = [3, 1]
f = findMin2(nums)
print(f)
