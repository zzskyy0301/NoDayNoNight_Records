'''讲解：https://www.youtube.com/watch?v=lm6pBga98-w
 桶排序
下面这个是我自己写的，不太快，可以后面看看怎么改进'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_freq={}
        for ele in nums:
            if ele in num_freq.keys():
                num_freq[ele]=num_freq[ele]+1
            else:
                num_freq[ele]=1
        
        freq_num={}
        for i in range(len(nums),0,-1):freq_num[i]=[]
        print(freq_num)
        for key,val in num_freq.items():
                freq_num[val].append(key)
        
        ans=[]
        c=0
        for j in range(len(nums),0,-1):
            
            if freq_num[j]!=0:
                ans.extend(freq_num[j])
                c+=len(freq_num[j])                
            if c>=k:
                break
        return ans
            

        



