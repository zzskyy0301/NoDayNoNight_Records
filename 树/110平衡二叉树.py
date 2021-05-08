# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if node==None:
                return 0
            else:
                leftl=dfs(node.left)
                rightl=dfs(node.right)
                return max(leftl,rightl)+1
        if not root:
            return True
        else:
            
            if abs(dfs(root.left)-dfs(root.right))<=1 and self. isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False
        
