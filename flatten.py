"""flatten
Write a recursive function called flatten which accepts an array of arrays and returns a new 
array with all values flattened.

Examples

flatten([1, 2, 3, [4, 5]]) # [1, 2, 3, 4, 5]
flatten([1, [2, [3, 4], [[5]]]]) # [1, 2, 3, 4, 5]
flatten([[1], [2], [3]]) # [1, 2, 3]
flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) # [1, 2, 3]"""

def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr 
           
"""capitalizeWords
Write a recursive function called capitalizeWords. 
Given an array of words, return a new array containing each word capitalized."""

def capitalizeWords(arr):
    # TODO

    
    if not arr:
        return

    if len(arr)==1:
        return [arr[0].upper()]
    else:    
       
        
        return [arr[0].upper()] + capitalizeWords(arr[1:])


"""stringifyNumbers
Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers
 and converts them to strings. Recursion would be a great way to solve this!"""

def stringifyNumbers(obj):
    # TODO
    
    if not obj:
        return
    
    new_obj = {}
    
    for key, value in obj.items():
        if type(value) is dict:
            new_obj[key] = stringifyNumbers(value)
        elif str(value).isdigit():
            new_obj[key] = str(value)
        else:
            new_obj[key] = value
    
    return new_obj