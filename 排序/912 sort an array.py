class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return
         
        self.quicksort(nums,0,len(nums)-1)
        return nums
    def quicksort(self,arr,start,end):
        if start>=end: return
        pivot=arr[(start+end)//2]
        left=start
        right=end
        while left<=right: #重点1：left<=right,为了防止partition之后有overlap
            while (left<=right) and arr[left]<pivot:#arr[left<pivot,不是<=,防止有重复元素
                left+=1
            while (left<=right) and arr[right]>pivot:
                right-=1
            if (left<=right):
                temp=arr[left]
                arr[left]=arr[right]
                arr[right]=temp
                left+=1
                right-=1
        self.quicksort(arr,start,right)#start，right
        self.quicksort(arr,left,end)
    
