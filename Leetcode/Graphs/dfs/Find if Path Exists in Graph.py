from collections import defaultdict
from email.policy import default
from pickle import TRUE
from this import d
from typing import List


class Solution:
    
    def dfs(self, graph, visit, source, dest):
        flag = False
        if source == dest:
            return True
        visit.add(source)
        
        for neightbour in graph[source]:
            if neightbour in visit:
                continue
            flag = self.dfs(graph, visit, neightbour, dest)
            if flag == True:
                return True
        return flag
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for edge in edges:
            vertex1 = edge[0]
            vertex2 = edge[1]
            graph[vertex1].append(vertex2) 
            graph[vertex2].append(vertex1) 
        
        visit = set()

        return self.dfs(graph, visit, source, destination)
    
    
class Solution2:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adjaceny_list = [[] for _ in range(n)]
        
        for edge in edges:
            adjaceny_list[edge[0]].append(edge[1])
            adjaceny_list[edge[1]].append(edge[0])
            
            
        seen = set()
        stack = [source]
        
        while(stack):
            node = stack.pop()
            if node == destination:
                return True
            if node in seen:
                continue
            
            seen.add(node)
           
            for neighbour in adjaceny_list[node]:    
                stack.append(neighbour)
        
        return False
        
sol = Solution2()#Solution()

print(sol.validPath(
    n = 3,
    edges = [[0,1],[1,2],[2,0]],
    source = 0, 
    destination = 2
))

print(sol.validPath(
   n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
))
