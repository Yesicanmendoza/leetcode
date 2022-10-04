""" Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once."""

def groupAnagrams(strs):
    class Solution(object):
        def groupAnagrams(self, strs):
            """
            :type strs: List[str]
            :rtype: List[List[str]]
            """
            result = defaultdict(list)
            
            for word in strs:
                result["".join(sorted(word))].append(word)
                
            return result.values()
            
    #         result = []
    #         indexes = set()
            
            
    #         for i in range(len(strs)):            
    #             a = list(strs[i])
    #             a.sort()
    #             lst = []
    #             if i not in indexes:
    #                 lst.append(strs[i])
    #                 indexes.add(i)
    #                 for index, word in enumerate(strs):
    #                     b = list(word)
    #                     b.sort()
                    

    #                     if index not in indexes and a == b:
    #                         lst.append(word)
    #                         indexes.add(index)
                
    #             if lst:
    #                 result.append(lst)
                
                    
    #         return result   
            

