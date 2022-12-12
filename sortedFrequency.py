
"""Given a sorted array and a number, write a function called sortedFrequency that counts the occurrences of the number in the array.

sortedFrequency([1, 1, 2, 2, 2, 2, 3], 2) # 4
sortedFrequency([1, 1, 2, 2, 2, 2, 3], 3) # 1
sortedFrequency([1, 1, 2, 2, 2, 2, 3], 4) # -1
sortedFrequency([], 4) # -1
Time Complexity - O(log n)"""

def sortedFrequency(arr, num):
    # TODO
    if not arr:
        return 0
        
    if len(arr) == 1:
        if num in arr:
            return 1
        return 0
    
    if arr[0] > num:
        return 0
    
        
    else:
        mid = len(arr)//2
        
        op1 = arr[:mid]
        op2 = arr[mid:]
        
        if op1[-1] < num:
            return sortedFrequency(op2, num)
        else:
            return sortedFrequency(op1, num) + sortedFrequency(op2, num)
