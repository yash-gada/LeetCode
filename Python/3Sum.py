# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        l = []
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i,len(nums)-1):
                for k in range(j, len(nums)):
                    if(nums[i] + nums[j] + nums[k] == 0) and (i!=j!=k):
                        l.append((nums[i], nums[j], nums[k]))
        
        return set(l)
        '''
        l = []
        p, n, z = [], [], []
        for i in nums:
            if(i>0):
                p.append(i)
            elif(i<0):
                n.append(i)
            else:
                z.append(i)

        P = set(p)
        N = set(n)

        if(z):
            for i in P:
                if(-1*i in N):
                    l.append((-1*i, 0, i))

        if(len(z)>=3):
            l.append((0, 0, 0))
        
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if(-1*(n[i]+n[j]) in P):
                    l.append( tuple(sorted([n[i], n[j], -1*(n[i]+n[j])])) )

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                if(-1*(p[i]+p[j]) in N):
                    l.append( tuple(sorted([p[i], p[j], -1*(p[i]+p[j])])) )

        return set(l)
