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

# 90. Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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

#39. Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total  == target:
                res.append(cur.copy())
                return
            if i >=len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [],0)
        return res

#40. Combination Sum II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        ans = []
        n = len(candidates)

        def backtrack(start, target, path):
            if target == 0:
                ans.append(path.copy())
                return
            if target < 0:
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return ans
