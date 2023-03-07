"""
最大子数组和
https://leetcode.cn/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            