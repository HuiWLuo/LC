# 230. Kth Smallest Element in a BST
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count =0
        self.result = None

        def in_order(node):
            if node is None or self.result is not None:
                return

            in_order(node.left)

            self.count +=1
            if self.count ==k:
                self.result = node.val
                return

            in_order(node.right)

        in_order(root)
        return self.result




# 199. Binary Tree Right Side View
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        right_view = []
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                
                if i == level_length - 1:
                    right_view.append(node.val)
                if node.right:
                    queue.append(node.right)
        
        return right_view
