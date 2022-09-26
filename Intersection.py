"""Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order."""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            arr1, arr2 = nums1, set(nums2)
        else:
            arr1, arr2 = nums2, set(nums1)
        
        
        
        
        result = set()
        
        for num in arr1:
            if num in arr2:
                result.add(num)
                
        return list(result)