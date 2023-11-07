# 1921. Eliminate Maximum Number of Monsters

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        if(len(dist) == 0):
            return 0
        
        time = list()
        for i in range(len(dist)):
            time.append(ceil(dist[i]/speed[i]))
        time.sort()
        cnt = 0
        for i in range(len(dist)):
            if(time[i] > i):
                cnt+=1
            else:
                return cnt
        return cnt
