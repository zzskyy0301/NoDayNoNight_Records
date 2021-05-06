# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        def dfs(node,path):
            if node:
                path=path+str(node.val)
                if node.left==None and node.right==None:#到达叶子
                    totalpath.append(path)
                else:
                    path+='->'
                    dfs(node.left,path)
                    dfs(node.right,path)
        totalpath=[]
        path=''
        dfs(root,path)
        return totalpath
