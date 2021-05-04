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
                result.append(track[:])
               
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
