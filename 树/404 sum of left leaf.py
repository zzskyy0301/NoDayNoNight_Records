# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def isleaf(node):
            if not node:
                return False
            if node.left==None and node.right==None:
                return True
            return False

        def search(node):
            if not node:
                return 0
            if isleaf(node.left):
                return ans+node.left.val+search(node.right)
            return ans+search(node.left)+search(node.right)
        ans=0
        return search(root)
