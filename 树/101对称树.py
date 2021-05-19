# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def ismirrow(node1,node2):
            if node1==None and node2==None:
                return True
            if node1==None or node2==None:
                return False
            return node1.val==node2.val and ismirrow(node1.left,node2.right) and ismirrow(node1.right,node2.left)
        if not root:
            return False
        return ismirrow(root.left,root.right)
