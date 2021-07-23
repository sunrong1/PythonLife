class Solution():
    def twoSum(self, nums, target):
        """
        方法1：字典方法
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in mapping:
                return [index, mapping[diff]]
            else:
                mapping[val] = index

        def twoSum2(self, nums, target):
            """
            方法1：字典方法
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            mapping = {}

            for index, val in enumerate(nums):
                diff = target - val
                if diff in mapping:
                    return [index, mapping[diff]]
                else:
                    mapping[val] = index
