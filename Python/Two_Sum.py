# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''
        #BRUTE FORCE

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]+nums[j] == target):
                    return i, j
        '''

        #USING HASHMAP --> LESSER TIME COMPLEXITY
        d = {}

        for i, first in enumerate(nums):
            second = target - first
            
            if(second in d):
                return d[second], i
            else:
                d[first] = i
        return False
