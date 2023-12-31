# 1441. Build an Array With Stack Operations

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        res = []
        p = 0

        for i in range(1, n+1):
            if(p < len(target)):
                if(target[p] == i):
                    res.append("Push")
                    p+=1
                else:
                    res.append("Push")
                    res.append("Pop")  
            else:
                break    
        return res
