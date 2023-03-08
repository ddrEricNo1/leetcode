"""
1.两数之和
https://leetcode.cn/problems/two-sum/?envType=study-plan&id=shu-ju-jie-gou-ru-men&plan=data-structures&plan_progress=xh9soo4c
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
            else:
                return [records[target - val], idx]