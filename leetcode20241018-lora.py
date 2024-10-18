# 283. Move zeros
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right]!= 0:
                nums[right], nums[left] = nums[left], nums[right]
                left +=1
        return nums

# 11. Container with most water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1        
        return max_area


# 1. two sum
class Solution:
    def twoSum(self, nums:List[int], target:int):
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


# 42.Trapping rainwater
class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right = len(height)-1
        left_max =height[left]
        right_max = height[right]
        water =0
        while left <right:
            if left_max <right_max:
                left += 1
                left_max = max(left_max,height[left])
                water +=left_max - height[left]
            else:
                right -=1
                right_max =max(right_max, height[right])
                water += right_max - height[right]
        return water
