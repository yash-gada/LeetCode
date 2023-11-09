# 1759. Count Number of Homogenous Substrings

class Solution:
    def countHomogenous(self, s: str) -> int:
        
        cnt = 0
        start = 0
        m = 1e9+7

        for i in range(len(s)):
            if(s[start] == s[i]):
                cnt += i - start + 1
            else:
                cnt+=1
                start = i
        return int(cnt%m)

        # FAILED INCOMPLETE ATTEMPTS BELOW
        '''
        test = ""#s[0]
        print(f"initial test = {test} \n\n")
        cnt = 0
        m = 1e9+7
        for i in range(len(s)):
            print(f"i = {s[i]}, test[-1] = {test[-1]}, test = {test}")
            if(s[i] != test[-1] or i == len(s)-1):
                cnt += (len(test) * (len(test) + 1)) / 2
                print(cnt, end="\n\n")
                
                test = s[i]
            else:
                test += s[i]
            
        return int(cnt % m)
        '''      

        '''
        l = sorted(s)
        print(s)
        print(f"SORTED LIST = {l}", end="\n\n")
        test = ""
        cnt = 0
        for i in l:
            
            test = test + i
            print(f"i = {i}, test = {test}")
            print(f"len of set = {len(set(test))}")

            if(len(set(test)) != 1):
                print("in if")
                test = test[-1]
            print("\n\n")

            for j in range(len(s) - len(test) + 1):
                print(f"s[j:j+len(test)] = {s[j:len(test)]}, test = {test}")
                if(s[j:j+len(test)] == test):
                    cnt+=1    
            
            #print(f"s.count(test) = {s.count(test)}")
            #cnt += s.count(test)

            print(f"cnt = {cnt}", end="\n\n")
        return cnt
        '''
