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
            pl=0
            pr=0
            l=path(node.left)
            r=path(node.right)
            if node.left and node.val==node.left.val :
                pl=l+1
            if node.right and node.val==node.right.val:
                pr=r+1
            self.ans=max(self.ans,pl+pr)
            return max(pl,pr)
        self.ans=0
        path(root)  
        return self.ans
