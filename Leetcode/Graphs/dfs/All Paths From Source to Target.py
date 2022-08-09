from typing import List

class Solution:
    def buildPaths(self, paths, output, curr, node):
        curr.append(node)
        if node == 0:
            output.append(reversed(curr))
            return
        for item in paths[node]:
            newlist = curr.copy()
            self.buildPaths(paths,output, newlist, item)def buildPaths(self, paths, output, curr, node) -> None:
        curr.append(node)
        if node == 0:
            output.append(reversed(curr))
            return
        for item in paths[node]:
            newlist = curr.copy()
            self.buildPaths(paths,output, newlist, item)
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        adjacency_list = [[] for _ in range(n)]
        
        for (index, dest) in enumerate(graph):
            adjacency_list[index] = dest
            
        seen = set()
        source = 0
        destination = n - 1
        stack = [source]
        paths = [[] for _ in range(n)]
        output = []
        while(stack):
            vertex = stack.pop()
            if vertex in seen:
                continue
            
            seen.add(vertex)
            
            
            for neighbour in adjacency_list[vertex]:
                paths[neighbour].append(vertex)
                stack.append(neighbour)
                
        for node in paths[n-1]:
            self.buildPaths(paths,output,[n-1], node)   
        
        return output
    
    
sol = Solution()
print(sol.allPathsSourceTarget(graph = [[1,2],[3],[3],[]]))
print(sol.allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]]))
