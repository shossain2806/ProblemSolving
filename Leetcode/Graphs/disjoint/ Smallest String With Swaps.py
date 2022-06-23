class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        root = [i for i in range(n)]
        rank = [1] * n
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x != root_y:
               if rank[root_x] > rank[root_y]:
                   root[root_y] = root_x
               elif rank[root_x] < rank[root_y]:
                   root[root_x] = root_y
               else:
                   root[root_y] = root_x
                   rank[root_x] += 1
     
                        
        for pair in pairs:
            union(pair[0], pair[1])
        
        roots = { }
        for vertex in range(n):
            rootNode = find(vertex)
            if roots.get(rootNode) == None:
                roots[rootNode] = [s[vertex]]
            else:
                roots[rootNode].append(s[vertex])        
        
        for k in roots:
            roots[k].sort()
        
        output = ""
        for index, element in enumerate(root):
            output += roots[element].pop(0)
        return output
    
sol = Solution()
print(sol.smallestStringWithSwaps("dcab",[[0,3],[1,2],[0,2]]))
