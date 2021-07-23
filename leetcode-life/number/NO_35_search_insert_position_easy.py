from typing import List


class Solution():
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        普通的二分方法
        :param nums:
        :param target:
        :return:
        """
        head = 0
        tail = len(nums) - 1
        while tail >= head:
            mid = (head + tail) // 2
            if nums[mid] > target:
                tail = mid - 1
            elif nums[mid] < target:
                head = mid + 1
            else:
                return mid
        return head


s = Solution()
print(s.searchInsert([0, 1, 2, ], 2))
