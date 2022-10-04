# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def detectCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         curr = head
        
#         viewed = set()
#         while curr:
#             if curr in viewed:
#                 return curr
#             else:
#                 viewed.add(curr)
#             curr = curr.next
            

def solution(S):
    # write your code in Python 3.6
    cam = 0
    cars = 0
    i_cars = []
    i_cam = []
    set_car = set('>', '<')
    for index, char in enumate(S):      

        if char in set_car:
            cars += 1
            i_cars.append(index)
        elif char == '.':
            cam += 1
            i_cam.append(index)

    if i_cars[0] > i_cam[0]:
        cam -= 1
    
    return cars*cam