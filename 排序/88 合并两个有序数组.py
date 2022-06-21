class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        k=0
        j=0
        i=0
        new=[]
        while (k<m or j<n):
            if k>=m:
                new.append(nums2[j])
                j+=1
            elif j>=n:
                new.append(nums1[k])
                k+=1
            elif nums1[k] < nums2[j]:
                new.append(nums1[k])
                k+=1
            else:
                new.append(nums2[j])
                j+=1
            i+=1
           # print(new)
        nums1[:]=new # list复制方法，不能直接写nums1=new, 讲解：https://zhuanlan.zhihu.com/p/89068120
        


        #if 和 elif 区别：如果是并排if，会遍历所有的if，这样会产生溢出
