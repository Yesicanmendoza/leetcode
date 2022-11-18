class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        
        for i, n in enumerate(nums):
            num = target - n
            if num in hmap:
                return [hmap[num], i]
            else:
                hmap[n] = i









