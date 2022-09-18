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
        curr = head
        
        while curr:
            temp = curr.next
            
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
                temp = curr
               
            curr = temp
                
        return head
        