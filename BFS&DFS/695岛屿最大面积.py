'''打败27%，还有更好的算法'''
class Solution(object):
    def findarea(self,grid,x,y):
            if  x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]!=1:
                return 0
            neighbor=[[0,-1],[0,1],[-1,0],[1,0]]
            grid[x][y]=0
            ans=1
            for nei in neighbor:
                dx=nei[0]
                dy=nei[1]
                ans+=self.findarea(grid,x+dx,y+dy)
            return ans
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]] grid[][]
        :rtype: int
        """
       # print(len(grid),len(grid[0]))
        area=0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                area=max(self.findarea(grid,i,j),area)
        return area



