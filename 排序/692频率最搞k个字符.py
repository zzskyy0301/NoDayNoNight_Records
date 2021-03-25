讲解：https://www.youtube.com/watch?v=POERw4yDVBw
  #方法一：
  class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count=Counter(words)
        candidates=count.keys()
        candidates.sort(key= lambda w: (-count[w],w)) #-coun[w]:按频率,w:按字母
        return candidates[:k]
#方法二：
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in xrange(k)]
