# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1

        for i in range(n-1):
            temp = a
            a = a + b
            b = temp
        return a


# 118. Pascal's Triangle
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        return triangle

  # 198. House Robber
  class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2, prev1 = prev1, current
        return prev1
