def heapify(arr,i):
      if i >=len(arr)-1:
          return arr
      son1=2*i+1
      son2=2*i+2
      maxin=i
      if son1<=(len(arr)-1) and arr[son1]>arr[maxin]:
          maxin=son1
      if son2<=(len(arr)-1) and arr[son2]>arr[maxin]:
          maxin=son2
      if maxin!=i:
        temp=arr[i]
        arr[i]=arr[maxin]
        arr[maxin]=temp
        heapify(arr,maxin)
      return arr
def build_heap(arr):
  lastparent_index=(len(arr)-2)//2
  #print(lastparent_index)
  for i in range(lastparent_index,-1,-1):
    #print(i)
    heapify(arr,i)
    #print(arr)
  return arr
def heap_sort(arr):
   arr=build_heap(arr)
   print(arr)
   for i in range(len(arr)-1,-1,-1):
     print(arr[i])
     temp=arr[0]
     arr[0]=arr[i]
     arr[i]=temp #arr[i]是最大值了
     print(arr[0:i])
     arr[0:i]=heapify(arr[0:i],0).copy() #对置换之后的进行heapify
     print('heapresult',arr)
   return arr
heap_sort([2,5,3,1,4,10])
