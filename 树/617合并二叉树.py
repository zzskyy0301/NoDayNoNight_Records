# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1==None:
            root1=root2
            return root1
        if root2==None:
            return root1
        else:
            root1.val=root1.val+root2.val
            root1.left=self.mergeTrees(root1.left,root2.left)
            root1.right=self.mergeTrees(root1.right,root2.right)
            return root1
