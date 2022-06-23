class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        ## n - 1 edges and connected then it must be valid tree
        edges_count = len(edges)
        
        if edges_count != n - 1:
            return False
        
        root = [i for i in range(n)]
        def find(x):
            return root[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                for i in range(n):
                    if root[i] == root_y:
                        root[i] = root_x
            
        for edge in edges:
            union(edge[0], edge[1])
            
        return len(set(root)) == 1