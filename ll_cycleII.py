# Definition for singly-linked list.
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
        curr = head
        
        viewed = set()
        while curr:
            if curr in viewed:
                return curr
            else:
                viewed.add(curr)
            curr = curr.next
            