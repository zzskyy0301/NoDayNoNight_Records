class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
           return False
        if root.left==None and root.right==None:
            return targetSum==root.val
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
