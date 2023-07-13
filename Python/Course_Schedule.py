# 207. Course Schedule

#This a tricky one. Go through DFS first to know the basics of this

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #The Courses are like nodes of a graph and Prerequisites give us the direction of the edge to new node.
        #THIS IS BASICALLY A DIRECTED GRAPH 

        #Initializing an empty list for every Course (node) to store Prerequisites 
        #Basically prereqMap is a HashMap
        prereqMap = { i:[] for i in range(numCourses)}

        #populating the HashMap
        for c, prereq in prerequisites:
            prereqMap[c].append(prereq)
        
        visited = set() #to store visited nodes

        print(prereqMap)

        def dfs(c): 
            #graph and visited are already available as this func is inside outer func

            print("c =", c)
            
            if(c in visited) == True: #checking if the node is already visited
                return False
            if(prereqMap[c] == []): #if node has no prereqs, course can be completed
                return True
            
            visited.add(c) 
            #if not visited AND has prereqs, this course is being visited
            print(visited)

            for pre in prereqMap[c]: #for each prereq of this course c
                print("\t", pre)
                if(dfs(pre) == False): 
                    #checking recursively DFS of the prereqs of c
                    return False 
                    #any prereqs failing is a complete fail

            visited.remove(c) 
                #if none of the prereqs failed, clear visited for next course
                
            prereqMap[c] = [] 
                #making it easy for next time we see the same course as it is already checked
            return True

        for c in range(numCourses):
            if(dfs(c) == False):
                return False
        return True
        
