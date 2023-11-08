# 2849. Determine if a Cell Is Reachable at a Given Time

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if((sx==fx and sy==fy) and t>1):
            return True
        elif((sx==fx and sy==fy) and t==1):
            return False
        
        #d = math.sqrt(math.pow(fy-sy, 2) + math.pow(fx-sx, 2))
        #print(d, round(d), t)

        d = max(abs(fy-sy), abs(fx-sx))

        if(d <= t):
            return True
        else:
            return False
