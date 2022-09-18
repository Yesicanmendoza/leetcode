# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        curr = head
        
        viewed = set()
        while curr:
            if curr in viewed:
                return True
            else:
                viewed.add(curr)
            curr = curr.next
            
        return False