class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #BFS:eliminate zeros every time
        # queue=[[0,0],[0,1]...[[n,n]]]
        # (x,y)->(x-1,y)(x+1,y)(x,y-1)(x,y+1)(x-1,y-1)(x-1,y+1)(x+1,y+1)(x+1,y-1)
        # vertex=grid[
        # if vertex==0:
        #     not add to queue
        # else:
        #     add to queue,seen,parent
        self.grid=grid
        n=len(grid)
        if len(grid)==1:
            return 1
        if grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1
        queue=deque()
        queue.append([0,0])
        path=1
        while queue:
            for _ in range(len(queue)):
                vertex=queue.popleft()
                x=vertex[0]
                y=vertex[1]
                neighbors=[[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1],
                                     [x, y + 1], [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]
                for nei in neighbors:
                            nei_x=nei[0]
                            nei_y=nei[1]
                            
                            if nei_x==(n-1) and nei_y==(n-1):
                                
                                return path+1
                            if -1<nei_x<=(n-1) and -1<nei_y<=(n-1):#小于等于王家的话，就会检索不到边界点
                                
                                if grid[nei_x][nei_y]==1:
                                    continue
                                if grid[nei_x][nei_y]==-1:
                                    continue
                                if grid[nei_x][nei_y]==0:
                                    
                                    queue.append([nei_x,nei_y])
                                    grid[nei_x][nei_y]=-1
                
            path+=1
 
        return -1
