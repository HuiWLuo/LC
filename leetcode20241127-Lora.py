#53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp =[0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
           dp[i] = max(dp[i-1] + nums[i], nums[i])
        res = float('-inf')
        for j in range(len(nums)):
            res = max(res, dp[j])
        return res
