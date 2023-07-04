# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        for i in range(1, len(nums)):
            if(nums[p] != nums[i]):
                p+=1
                nums[p] = nums[i]
        return p+1
