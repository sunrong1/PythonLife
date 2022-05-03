from typing import List

"""
三数之和
算法设计：
最重要的是首先进行排序，减少查找的复杂度；
nums = [-1,0,1,2,-1,-4]
排序后= [-4,-1,-1,0,1,2]
i 循环：
    l = i+1
    r = n-1
    遇到重复的，前进到最后一个
    
"""


def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    length = len(nums)
    nums.sort()

    ret = list()
    i = 0
    while i < length - 1:
        # 优化1,第一个数>0 后面的数不用看了
        if nums[i] > 0:
            break
        # 保证不能重复,多个重复的数，用第一个就可以
        # if i > 0 and nums[i - 1] == nums[i]:
        #     i += 1
        #     continue

        # 双子针方法，左右同时移动
        r = length - 1
        l = i + 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                if ret.count([nums[i], nums[l], nums[r]]) < 1:
                    ret.append([nums[i], nums[l], nums[r]])
                    # 去除重复的
                while l + 1 < r and nums[l] == nums[l + 1]:
                    l = l + 1
                while r - 1 > l and nums[r] == nums[r - 1]:
                    r = r - 1
                # 同时移动，一个增加，一个减少
                l = l + 1
                r = r - 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r = r - 1
            else:
                l = l + 1
        i += 1
    return ret


def threeSum1(nums: List[int]) -> List[List[int]]:
    """
    方法1：双指针法,重点是去重，排序降维
    目标值为0,答案中不可以包含重复的三元组
    :type nums: List[int]
    :rtype: List[List[int]
    """
    length = len(nums)
    if length < 3:
        return []
    nums.sort()
    i = 0
    result = []
    if nums[0] > 0:
        return []
    for i in range(length):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = length - 1
        while l < r:
            target = -nums[i]
            if l > i + 1 and nums[l] == nums[l - 1]:
                l += 1
                continue
            if r < length - 1 and nums[r] == nums[r + 1]:
                r -= 1
                continue
            if (l >= r):
                break
            if nums[l] + nums[r] == target:
                result.append([nums[i], nums[l], nums[r]])
            if nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return result


"""
第二次练习：
思路更清晰，位置更准确；

去重可以进行特殊处理，减少操作，但是效率较低
"""


def threeSum2(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    ret = []
    nums.sort()
    length = len(nums)
    i = 0
    while i <= length - 1:
        l = i + 1
        r = length - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                ret.append([nums[i], nums[l], nums[r]])
                while l + 1 <= length - 1 and nums[l] == nums[l + 1]:
                    l += 1
                l += 1
                r -= 1

            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1
        while i + 1 <= length - 1 and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return ret


nums = [-1, 0, 1, 2, -1, -4]
nums = [-4, -1, -1, 0, 1, 2]
nums = [0, 0, 0, 0]

nums = [-2, 0, 0, 2, 2]
a = threeSum2(nums)
print(a)
