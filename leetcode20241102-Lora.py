#98. Validate Binary Search Tree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, left=float('-inf'), right=float('inf')):
            if not root:
                return True

            if root.val <= left or root.val >= right:
                return False
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)

        return helper(root)


# 437. Path Sum III
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        self.res = 0
        self.cur_sum =0
        def helper(root):
            if not root:
                return
            self.cur_sum +=root.val
            self.res += prefix[self.cur_sum - targetSum]
            prefix[self.cur_sum] +=1
            helper(root.left) 
            helper(root.right)
            prefix[self.cur_sum] -= 1
            self.cur_sum -= root.val
        helper(root)
        return self.res   
