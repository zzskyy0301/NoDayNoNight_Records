#题目：https://www.bilibili.com/video/BV18x411V7fm?from=search&seid=17634974020751439362
import numpy as np
def maxsalary(time,value):
  #time:[0,3],[1,4]...
  #value:3,5,8...
  #找到prev[i]
  prev=np.zeros(len(time))
  prev[0]=int(0)
  for i in range(len(time),0,-1):
    for j in range(i-1,-1,-1):
     
      if time[j][1]<=time[i-1][0]:
        prev[i-1]=int(j+1)
        break
  
  #找到OPT[I]=max{opt[prev[i]]+value[i], opt[i-1]}
  OPT=[[] for i in range(len(time)+1)]#这里加1，是因为如果previous tasks没有，OPT=0
  OPT[0]=0
  OPT[1]=val[0]
  tasksdo=[[] for i in range(len(time)+1)]#这里也要加1，当从第一个tasks开始看的时候，do task->需要tasksdo[task-1]上加task1
  tasksdo[0]=[]
  

  for task in range(1,len(value)+1):
   
    OPT_DO=val[int(task-1)]+OPT[int(prev[task-1])]
    OPT_NOTDO=OPT[task-1]  

    if OPT_DO>=OPT_NOTDO:
      
      OPT[task]=OPT_DO
      
      tasksdo[task]=tasksdo[int(prev[task-1])].copy()#这里要用copy,不能用等号，不然会把tasksdo[int(prev[task-1])]的值改变
      tasksdo[task].append(task)
  
    else:
      
      OPT[task]=OPT_NOTDO
      tasksdo[task]=tasksdo[task-1]
    
  return OPT[-1],tasksdo[-1]
time=[[1,4],[3,5],[0,6],[4,7],[3,8],[5,9],[6,10],[8,11]]
val=[5,1,8,4,6,3,2,4]
maxsalary(time,val)
