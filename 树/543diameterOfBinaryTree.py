# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def depth(node):
            
            if node==None:
                return 0
            left=depth(node.left)
            right=depth(node.right)
            self.ans=max(self.ans,left+right+1)
            return max(left,right)+1
        self.ans=1
        depth(root)
        return self.ans-1
