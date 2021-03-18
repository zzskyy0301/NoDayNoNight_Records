class node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=node()
    def length(self):
        l=0
        cur=self.head
        while cur.next!=None:
            cur=cur.next
            l+=1
        return l

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index>=self.length() or index<0: # added 'index<0' post-video
			print("ERROR: 'Get' Index out of range!")
			return -1
        # cur_node=self.head
        # for i in range(index+1):
        #     cur_node=cur_node.next
        #     return cur_node.val
        if (index>=self.length()) or (index<0):return -1
        cur_index=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_index==index:
                return cur_node.val
            cur_index+=1
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0,val)

    def display(self):
        cur_node=self.head()
        elem=[]
        for i in range(self.length()):
            cur_node=cur_node.next()
            elem.append(cur_node.val)
        print(elem)



    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.length(),val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index>=self.length() or index<0:
			print('error')
           
        cur_node=self.head
        prior_node=self.head
        cur_idx=0
        while True:
            cur_node=cur_node.next
            if cur_idx==index: 
                new_node=node(val)
                prior_node.next=new_node
                new_node.next=cur_node
                return
            prior_node=cur_node
            cur_idx+=1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if (index>=self.length()) or (index<0):return 
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # delete pred.next 
        pred.next = pred.next.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
