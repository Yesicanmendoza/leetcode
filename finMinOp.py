def findMinOperationBU(s1, s2, index1, index2, tempDict):
    
    if index1 == len(s1):
        return len(s2)-index2
    if index2 ==len(s2):
        return len(s1)-index1
    if s1[index1] == s2[index2]:
        return findMinOperationBU(s1, s2, index1+1, index2+1,tempDict)
    
    tempKey = str(index1)+ str(index2)
    if tempKey not in tempDict:
        
        delete = 1 + findMinOperationBU(s1, s2, index1, index2+1,tempDict)
        insert = 1 +findMinOperationBU(s1, s2, index1+1, index2,tempDict)
        replace = 1 + findMinOperationBU(s1, s2, index1+1, index2+1,tempDict)
        
        tempDict[tempKey]= min(delete, insert, replace)
    
    return tempDict[tempKey]