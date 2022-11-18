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

    dic = {"page":null,"per_page":10,"total":99,"total_pages":10,"data":[{"id":1,"timestamp":1565637002408,"diagnosis":{"id":3,"name":"Pulmonary embolism","severity":4},"vitals":{"bloodPressureDiastole":154,"bloodPressureSystole":91,"pulse":125,"breathingRate":32,"bodyTemperature":100},"doctor":{"id":2,"name":"Dr Arnold Bullock"},"userId":2,"userName":"Bob Martin","userDob":"14-09-1989","meta":{"height":174,"weight":172}},{"id":2,"timestamp":1562539731129,"diagnosis":{"id":4,"name":"Pleurisy","severity":3},"vitals":{"bloodPressureDiastole":139,"bloodPressureSystole":81,"pulse":104,"breathingRate":20,"bodyTemperature":99.4},"doctor":{"id":2,"name":"Dr Arnold Bullock"},"userId":2,"userName":"Bob Martin","userDob":"14-09-1989","meta":{"height":174,"weight":171}},{"id":3,"timestamp":1563465027370,"diagnosis":{"id":2,"name":"Common Cold","severity":1},"vitals":{"bloodPressureDiastole":125,"bloodPressureSystole":76,"pulse":113,"breathingRate":22,"bodyTemperature":100.8},"doctor":{"id":4,"name":"Dr Allysa Ellis"},"userId":2,"userName":"Bob Martin","userDob":"14-09-1989","meta":{"height":174,"weight":185}},{"id":4,"timestamp":1561018581520,"diagnosis":{"id":4,"name":"Pleurisy","severity":3},"vitals":{"bloodPressureDiastole":138,"bloodPressureSystole":80,"pulse":124,"breathingRate":22,"bodyTemperature":97},"doctor":{"id":2,"name":"Dr Arnold Bullock"},"userId":4,"userName":"Francesco De Mello","userDob":"02-05-1994","meta":{"height":183,"weight":185}},{"id":5,"timestamp":1557725281296,"diagnosis":{"id":3,"name":"Pulmonary embolism","severity":4},"vitals":{"bloodPressureDiastole":153,"bloodPressureSystole":99,"pulse":124,"breathingRate":34,"bodyTemperature":102.5},"doctor":{"id":4,"name":"Dr Allysa Ellis"},"userId":4,"userName":"Francesco De Mello","userDob":"02-05-1994","meta":{"height":183,"weight":210}},{"id":6,"timestamp":1568550058964,"diagnosis":{"id":3,"name":"Pulmonary embolism","severity":4},"vitals":{"bloodPressureDiastole":155,"bloodPressureSystole":90,"pulse":130,"breathingRate":29,"bodyTemperature":99.2},"doctor":{"id":2,"name":"Dr Arnold Bullock"},"userId":1,"userName":"John Oliver","userDob":"02-01-1986","meta":{"height":168,"weight":173}},{"id":7,"timestamp":1564691138999,"diagnosis":{"id":3,"name":"Pulmonary embolism","severity":4},"vitals":{"bloodPressureDiastole":147,"bloodPressureSystole":100,"pulse":138,"breathingRate":25,"bodyTemperature":100},"doctor":{"id":3,"name":"Dr Pilar Cristancho"},"userId":1,"userName":"John Oliver","userDob":"02-01-1986","meta":{"height":168,"weight":196}},{"id":8,"timestamp":1562157191823,"diagnosis":{"id":2,"name":"Common Cold","severity":1},"vitals":{"bloodPressureDiastole":122,"bloodPressureSystole":77,"pulse":91,"breathingRate":20,"bodyTemperature":101.5},"doctor":{"id":3,"name":"Dr Pilar Cristancho"},"userId":1,"userName":"John Oliver","userDob":"02-01-1986","meta":{"height":168,"weight":175}},{"id":9,"timestamp":1548036340751,"diagnosis":{"id":3,"name":"Pulmonary embolism","severity":4},"vitals":{"bloodPressureDiastole":147,"bloodPressureSystole":96,"pulse":130,"breathingRate":28,"bodyTemperature":101},"doctor":{"id":2,"name":"Dr Arnold Bullock"},"userId":3,"userName":"Helena Fernandez","userDob":"23-12-1987","meta":{"height":157,"weight":106}},{"id":10,"timestamp":1562161672195,"diagnosis":{"id":2,"name":"Common Cold","severity":1},"vitals":{"bloodPressureDiastole":127,"bloodPressureSystole":78,"pulse":130,"breathingRate":22,"bodyTemperature":103.8},"doctor":{"id":4,"name":"Dr Allysa Ellis"},"userId":3,"userName":"Helena Fernandez","userDob":"23-12-1987","meta":{"height":157,"weight":110}}]}