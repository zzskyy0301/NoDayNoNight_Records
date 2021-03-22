#归并排序
arr=[6,8,9,10,2,3,4,5]
def merge_sort(arr,l,m,r): #目的：对两个有序数列进行合并排序
  leftlist=[]#np.zeros(m-l+1)
  rightlist=[]#np.zeros(r-m)
  for i in range(l,m+1):
    leftlist.append(arr[i])
  for j in range(m+1,r+1):
    rightlist.append(arr[j])
  #print(leftlist,rightlist)
  k=l
  i=0
  j=0
  while i<m-l+1 and j<r-m:
    
    if leftlist[i]<rightlist[j]:

      arr[k]=leftlist[i]
      k+=1
      i+=1
    else:
      arr[k]=rightlist[j]
      k+=1
      j+=1
  if i==m-l: 
    while j<r-m:
      arr[k]=righlist[j]
      k+=1
      j+=1
  if j==r-m: 
    while i<m-l+1:
      arr[k]=leftlist[i]
      k+=1
      i+=1
  return arr
def merge_random(arr,l,r):#目的：从中间分开两个有序的数列后，进行排序
  if l==r:
    return arr
  else:
    m=(l+r)//2
    arr=merge_random(arr,l,m)
    print(arr)
    arr=merge_random(arr,m+1,r)
    print(arr)
    arr=merge_sort(arr,l,m,r)
  return arr


merge_random(arr,0,len(arr)-1)
