# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))[::-1]
        r = 0
        if(x<0):
            r = int(s)-(2*int(s))
        else:
            r = int(s)

        if(-2147483648<=r<=2147483648):
            return r
        else:
            return 0
