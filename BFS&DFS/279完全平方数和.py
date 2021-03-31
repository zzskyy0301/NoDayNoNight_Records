'''方法一：会超出时间限制，动态规划'''
import math
class Solution(object):
  
    def numSquares(self,n):
        sqlist=[i**2 for i in range(1,int(math.sqrt(n))+1)]#别忘了加一,因为INT是四舍五入的
        #print(sqlist)
        def midsolution(n):
            if n in sqlist:
                return 1
            cur_min=float('inf')
            for k in sqlist:
                if n<k:
                    break #这里要加一下break，以防止k>n
                #print(k,midsolution(n-k)+1)
                cur_min=min(midsolution(n-k)+1,cur_min)
            return cur_min

        return midsolution(n)
      
  '''方法二：BFS，不会超出限制'''
  
        
