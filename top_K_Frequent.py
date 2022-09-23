""" Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1] """

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()
        dic = {}
        mval = 0
        for n in nums:
            dic[n] =1+ dic.get(n, 0)
            mval = max(mval, dic[n])
            #print('mval, n', mval, n)
            
        
        result = []
        items = 0
        times = 0
        while times < k:
            for n, val in dic.items():
                if val == mval:
                    result.append(n)
            #print('mval', mval)
            #print('result', result)
            #print('times', times)
            times = len(result)   
            mval-=1
            
        
        
        return result
                