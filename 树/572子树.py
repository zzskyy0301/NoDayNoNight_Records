# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def sametree(node1,node2):
            if node1==None and node2==None:
                return True
            if not node1 or not node2:
                return False
            if node1.val!=node2.val:
                return False
            return sametree(node1.left,node2.left) and sametree(node1.right,node2.right)
        
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return sametree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
