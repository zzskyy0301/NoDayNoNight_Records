讲解：https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def backtrack(nums,visited):
            if len(track)==len(nums):
                result.append(track[:])
                return
            for i in range(len(nums)):
                if visited[i]==True:
                    continue        
                if i>0 and nums[i]==nums[i-1] and visited[i-1]==False:
                    continue
                track.append(nums[i])          
                visited[i]=True                           
                backtrack(nums,visited)
                visited[i]=False
                track.pop()
        track=[]
        nums.sort()#先sort
        visited=[0 for i in range(len(nums))]
        result=[]
        backtrack(nums,visited)
        return result
