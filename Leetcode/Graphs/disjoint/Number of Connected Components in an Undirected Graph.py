class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def find(root, x):
            return root[x]
        
        def union(root, nodes, x, y):
            root_x = find(root, x)
            root_y = find(root, y)
            if root_x != root_y:
                for i in range(nodes):
                    if root[i] == root_y:
                        root[i] = root_x
                    
        root = [i for i in range(n)]
        
        for edge in edges:
            union(root, n, edge[0], edge[1])
        
        return len(set(root))