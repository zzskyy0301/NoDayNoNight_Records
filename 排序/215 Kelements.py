class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if (nums==None or len(nums)==0): return []
        l=0
        r=len(nums)-1
        k=len(nums)-k
        while (l<=r):
            mid=self.quick_sort(nums,l,r)
            if mid==k:
                return nums[k]
            elif mid>k:
                r=mid-1
            else:
                l=mid+1
        return nums[k]

    def quick_sort(self,nums,l,r):
        pivot=nums[r]
        i=l-1
        for j in range(l,r):
            if (nums[j]<pivot):
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
        nums[i+1],nums[r]=nums[r],nums[i+1]
        return i+1

作者：geng-chen-i
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/pythonkuai-pai-by-geng-chen-i-uo9c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''堆排序算法'''
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

arr=build_heap(arr)
print(arr)
for i in range(len(arr)-1,-1,-1):

    temp=arr[0]
    arr[0]=arr[i]
    arr[i]=temp
    if i==len(arr)-k:
        return arr[i]
    else:
        arr[0:i]=heapify(arr[0:i],0)[:]


return nums[[len(arr)-k]]

