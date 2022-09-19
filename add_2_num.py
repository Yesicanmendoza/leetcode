class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode()
        curr = result
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry
            if carry == 1:
                carry = 0
            if val >= 10:
                val -=10
                carry = 1
                
            new_node = ListNode(val)
            curr.next = new_node
            
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            curr = curr.next
        
        
        return result.next