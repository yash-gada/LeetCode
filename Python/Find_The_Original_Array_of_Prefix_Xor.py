# 2433. Find The Original Array of Prefix Xor

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        if(len(pref) == 0):
            return None
        if(len(pref) == 1):
            return pref

        xor = []
        xor.append(pref[0])
        check = pref[0]
        
        for i in range(1, len(pref)):
            xor.append(check^pref[i])
            check = check^xor[-1]

        return xor
