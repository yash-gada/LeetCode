# 1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #p = 0
        l = [0]
        for i in gain:
            #p+=i
            l.append(l[-1]+i)
        return max(l)
