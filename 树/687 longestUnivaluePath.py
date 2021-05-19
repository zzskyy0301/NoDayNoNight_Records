# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def path(node):
            if not node:
                return 0
            left=right=0
            if node.left and node.val==node.left.val :
                left=path(node.left)+1
            if node.right and node.val==node.right.val:
                right=path(node.right)+1
            self.ans=max(self.ans,left+right)
            return max(left,right)
        self.ans=0
        path(root)  
        return self.ans
