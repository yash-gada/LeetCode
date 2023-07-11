# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0

        nums1 += nums2 
        nums1.sort()
        #le = len(nums1)
        if(len(nums1)%2==0):
            median = ( nums1[len(nums1)//2] + nums1[(len(nums1)//2)-1] )/2
        else:
            median = nums1[len(nums1)//2]
        
        return float(median)
