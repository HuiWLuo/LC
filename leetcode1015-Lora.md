# leetcode53
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

# leetcode56
class Solution:
    def merge(self, intervals: List[List[int]) -> List[List[int]:
        if not intervals:
            return[]
        res = []
        intervals.sort(key = lambda itv: itv[0])
        left, right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if right < intervals[i][0]:
                res.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
            else:
                right = max(right, intervals[i][1])
        res.append([left, right])
        return res


# leetcode189
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        l, r =0, len(nums) -1
        nums[:] = nums[-k:] +nums[:-k]
