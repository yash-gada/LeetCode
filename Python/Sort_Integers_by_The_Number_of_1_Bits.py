# 1356. Sort Integers by The Number of 1 Bits

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        b_arr = list(map(bin, arr))

        ans = []
        for i in range(len(arr)):
            ans.append((arr[i], b_arr[i].count("1")))

        ans.sort(key = lambda x:(x[1], x[0]), reverse=False)

        return [i[0] for i in ans]

        '''
        # Easier, same time complexity
        
        arr.sort(key = lambda x: (bin(x).count("1"), x) )
        return arr
        '''
