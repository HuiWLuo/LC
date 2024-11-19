# 47. Permutations II
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res

  # 78. Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        result = []
        backtrack(0, [])
        return result

# 77. Combinations
  class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(start):
            if start==len(nums):
                if nums not in res:
                    res.append(nums[:])
                return
            
            for i in range(start,len(nums)):
                nums[start],nums[i] = nums[i],nums[start]
                backtrack(start+1)
                nums[start],nums[i] = nums[i],nums[start]
        backtrack(0)
        return res
