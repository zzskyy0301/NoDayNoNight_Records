class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        track=[]
        
        def backtrack(nums):
            if len(track)==len(nums):
                result.append(track[:])#这里一定要做一次拷贝，不然传递的是位置，最后返回空列表
               
               # return 
            for i in range(0,len(nums)):
                if nums[i] not in track:
                    track.append(nums[i])
                    backtrack(nums)
                    track.pop()
                    #print(result)
            #return result
        backtrack(nums)
        return result

    
    
            def backtrack(nums):
            if len(track)==len(nums):
                result.append(track[:])
               
                return
            for i in range(len(nums)):        
                if nums[i] not in track:
                    track.append(nums[i]) 
                                     
                    backtrack(nums)
                    track.pop()
        track=[]
        visited=[0 for i in range(len(nums))]
        result=[]
        backtrack(nums)
        return result
