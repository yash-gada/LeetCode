# 1232. Check If It Is a Straight Line

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, x2 = coordinates[0][0], coordinates[1][0]
        y1, y2 = coordinates[0][1], coordinates[1][1]
        if(y2 == y1 == 0):
            #both points on x axis
            slope = 0
        elif(x2 == x1):
            #both points parallel to y axis -> slope infinity... we take arbitrary no. 8(wink wink)
            slope = 8
        elif(x2==x1 and y2==y1):
            slope = 1
        else:
            slope = (y2 - y1)/(x2 - x1)

        n = len(coordinates)
        for i in range(1, n-1):
            for j in range(1):
                x1, x2 = coordinates[i][j], coordinates[i+1][j]
                y1, y2 = coordinates[i][j+1], coordinates[i+1][j+1]
                
                if(y2 == y1 == 0):
                    #both points on x axis
                    new_slope = 0
                elif(x2 == x1):
                    #both points parallel to y axis -> slope infinity... we take arbitrary no. 8(wink wink)
                    new_slope = 8
                elif(x2==x1 and y2==y1):
                    new_slope = 1
                else:
                    new_slope = (y2 - y1)/(x2 - x1)

                
                if(new_slope == slope):
                    continue
                else:
                    return False
                    
        return True
