# 501. Find Mode in Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = dict()
        p = root

        def explore(pointer):
            
            if(pointer.val is not None):
    
                if(pointer.val in d.keys()):
                    d[pointer.val]+=1
                else:
                    d[pointer.val]=1
    
                if(pointer.left):                    
                    explore(pointer.left)

                if(pointer.right):
                    explore(pointer.right)

        explore(p)
        
        sorted_d = sorted(d.items(), key=lambda x:x[1], reverse=True)

        m = [sorted_d[i][1] for i in range(len(sorted_d))]
        m = max(m, default=0)

        return [sorted_d[i][0] for i in range(len(sorted_d)) if(sorted_d[i][1] == m)]       
