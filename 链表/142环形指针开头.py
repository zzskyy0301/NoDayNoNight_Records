#讲解https://www.bilibili.com/video/BV14t411P77x?from=search&seid=659419480804250534
# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fast,slow=head,head
        while True:
            if fast.next==None or fast.next.next==None:
                return None
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
    
        return slow
    #妙处：相遇之后把慢指针移动回起点
