# 1688. Count of Matches in Tournament

class Solution:
    def numberOfMatches(self, n: int) -> int:
        '''
        # USING PROGRAM LOGIC
        
        cnt = 0

        while(n>1):
            cnt += n//2

            if(n % 2 == 0):
                n = n//2
            else:
                n = ((n-1)//2) + 1

        return cnt
        '''
      
        # Using Math Trick   
        return n-1
