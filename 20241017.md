#leetcode 238
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res =[0]*n
        prefix, suffix = [1]*(n+1), [1]*(n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(n-1, -1, -1):
            suffix[j] = suffix[j+1] * nums[j]
        for h in range(n):
            res[h] = prefix[h] * suffix[h+1]
        return res
        

#leetcode 560
class Solution(object):
    def subarraySum(self, nums, k):
        dic = {0:1}
        sums, res = 0, 0
        for num in nums:
            sums += num
            res +=dic.get(sums-k, 0)
            dic[sums] = dic.get(sums, 0) +1
        return res
