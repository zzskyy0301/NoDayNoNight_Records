# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur=head
        while cur.next!=None and cur!=None:
            if cur.val!=cur.next.val:
                cur=cur.next
            else:
                cur.next=cur.next.next
        return head


