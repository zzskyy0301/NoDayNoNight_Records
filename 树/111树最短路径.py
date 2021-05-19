# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def path(node):
            if not node:
                return float('inf')
            if node.left==None and node.right==None:
                return 1
            le=1
            leftpath=path(node.left)
            rightpath=path(node.right)
            le=le+min(leftpath,rightpath)
            return le
        if not root:
            return 0
