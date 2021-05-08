class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node==None:
                return 0
            else:
                left_l=dfs(node.left)
                right_l=dfs(node.right)
                return max(left_l,right_l)+1
            
        return dfs(root)
