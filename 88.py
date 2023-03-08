"""
88.合并两个有序数组
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 从后往前遍历
        while m and n:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1]=nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] =nums1[m-1]
                m -= 1
        while n:
            nums1[n-1]=nums2[n-1]
            n -= 1