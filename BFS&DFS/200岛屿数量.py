26%，有更优秀的解法
class Solution(object):
    
    def findarea(self,grid,x,y):
            neighbor=[[0,-1],[0,1],[-1,0],[1,0]]
            grid[x][y]=0
            for nei in neighbor:
                dx=nei[0]
                dy=nei[1]
                if  0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy]=='1':
                    self.findarea(grid,x+dx,y+dy)
    def numIslands(self,grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0 or len(grid[0])==0:
            return 0
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    
                    self.findarea(grid,i,j)
                    ans+=1
        return ans
