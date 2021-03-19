#讲解https://www.bilibili.com/video/av61002976/
快慢指针法
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: 
            return False
            #we can use if not expression to conditionally execute a block of statements only if the value is not empty or not False.
        slow,fast=head,head
        while(True):
            if fast.next==None or fast.next.next==None:
                return False
            
            fast=fast.next.next
            slow=slow.next
            if fast==slow: 
                return True
              #注意：先移动指针再判断
