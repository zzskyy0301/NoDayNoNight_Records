class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(num):
            if len(track)==k:
                ret.append(track[:])
                return
            
            for i in range(num,n+1):
                if i not in track:
                    track.append(i)
                    
                    backtrack(i+1)
                    track.pop()
        if k==0:
            return None
        else:
            ret=[]
            track=[]
            backtrack(1)
            return ret
