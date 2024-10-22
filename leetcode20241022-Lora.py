
# 1. Two Sum
class Solution:
    def twoSum(self, nums:List[int], target:int):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

#49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for word in strs:
            letters = [0] * 26
            for letter in word:
                letters[ord(letter) -ord('a')] +=1
            letters = tuple(letters)
            seen[letters].append(word)
        res = []
        for key, value in seen.items():
            res.append(value)
        return res

#128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res =0
        for num in nums:
            if num-1 not in nums:
                cur_len = 1
                cur_num = num
                while cur_num +1 in nums:
                    cur_len +=1
                    cur_num +=1
                res = max(res, cur_len)
        return res
