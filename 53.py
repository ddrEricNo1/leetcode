"""
最大子数组和
https://leetcode.cn/problems/maximum-subarray/

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 

"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)