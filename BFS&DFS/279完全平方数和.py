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
  
        
import math
class Solution(object):
    def numSquares(self,n):
        sqlist=[i**2 for i in range(1,int(math.sqrt(n))+1)]#别忘了加一
        #print(sqlist)
        path_l=0
        queue=[n]
        if n in sqlist :
                return 1
        while len(queue)!=0:
            path_l+=1
            print(queue,path_l)
            #node=queue.pop(0)
            sub_queue=[]
            for node in queue:
                for sqnum in sqlist:
                    if sqnum>=node:
                        break
                    else:
                        remains=node-sqnum
                        print(node,sqnum,path_l)
                        if remains in sqlist and path_l!=1:
                            return path_l+1
                        elif remains in sqlist and path_l==1:
                            return path_l+1
                        else:
                            sub_queue.append(remains)
            queue=sub_queue
