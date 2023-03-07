"""
最大子数组和
https://leetcode.cn/problems/maximum-subarray/

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 

"""

# 动态规划
"""
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)
"""



# 分治
def maxSubArray(nums, low, high):
    if low == high:
        return [low, high, nums[low]]
    else:
        mid = (low + high) // 2
        [left_low, left_high, left_sum] = maxSubArray(nums, low, mid)
        [right_low, right_high, right_sum] = maxSubArray(nums, mid + 1, high)
        [cross_low, cross_high, cross_sum] = find_max_crossing_subarray(nums, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return [left_low, left_high, left_sum]

        if right_sum >= left_sum and right_sum >= cross_sum:
            return [right_low, right_high, right_sum]
        
        if cross_sum >= left_sum and cross_sum >= right_sum:
            return [cross_low, cross_high, cross_sum]
        

def find_max_crossing_subarray(array, low, mid, high) -> int:
    left_sum = -float("inf")
    right_sum = -float("inf")
    max_left = mid
    max_right = mid + 1
    sum = 0
    for i in range(mid, low-1, -1):
        sum = sum + array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    
    sum = 0
    for i in range(mid + 1, high + 1, 1):
        sum = sum + array[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return [max_left, max_right, left_sum + right_sum]


if __name__ == "__main__":
    [low, high, sum] = maxSubArray([-2,1,-3,4,-1,2,1,-5,4], 0, 8)
    print(low, high, sum)
