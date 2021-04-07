class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #边界上：不管
        #紧邻边界：判断四周是否与‘O’相连，不相连的改
        if not board:
            return
        m=len(board)
        n=len(board[0])
        def dfs(x,y):
            if x<0 or x>m-1 or y<0 or y>n-1 or board[x][y]!='O':
                return
            
            board[x][y]='A'
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n-1):
            dfs(0,j)
            dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="A":
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'


