# 1877. Minimize Maximum Pair Sum in Array

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        new = sorted(nums)
        m = new[1] + new[0]

        j = len(new)-1
        i = 0
        while(i<j):
            if(new[i]+new[j] > m):
                m = new[i]+new[j]

            j-=1
            i+=1
            
        return m
