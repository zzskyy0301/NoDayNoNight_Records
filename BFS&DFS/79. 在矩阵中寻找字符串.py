花花酱讲解：https://www.youtube.com/watch?v=oUeGFKZvoo4
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i,j,k):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False

            if k>=len(word):
                return False
            if board[i][j]!=word[k]:
                return False
            if k==len(word)-1 :
                return True
            char=board[i][j] #一个技巧：防止多次访问之前访问过的，把访问郭的设置为0，但要记得递归结束之后设置回原来的值，因为之后可能还要用。
            board[i][j]=0
            ret = dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1)
            board[i][j]=char
            return ret

        for i in range (len(board)):
            for j in range(len(board[0])):
                
                if dfs(i,j,0):
                    return True
        return False
        
   
