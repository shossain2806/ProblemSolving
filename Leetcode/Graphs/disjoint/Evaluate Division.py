from collections import defaultdict
from traceback import print_tb
from typing import Dict, List

    
class Solution:
    
    def dfs(self, graph, visits, product, source, dest):
        ret = -1.0
        visits.add(source)
        neighbours = graph[source]
        if dest in neighbours:
            return product * neighbours[dest]
        
        for neightbour in neighbours:
            if neightbour in visits:
                continue
            ret = self.dfs(graph, visits, product * neighbours[neightbour], neightbour, dest)
            if ret != -1.0:
                break
        visits.remove(source)
        return ret
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dfs_graph = defaultdict(defaultdict)
        output = []
        for (index, equation) in enumerate(equations):
           dividend = equation[0]
           divisor = equation[1]
           divison = float(values[index])
           dfs_graph[dividend][divisor] = float(divison)
           dfs_graph[divisor][dividend] = float(1.0 / divison)
        
        for query in queries:
            dividend = query[0]
            divisor = query[1]
            
            if dividend not in dfs_graph or divisor not in dfs_graph:
                output.append(-1.0)
            
            elif dividend == divisor:
                output.append(1.0)
            else:
                visits = set()
                output.append(self.dfs(dfs_graph, visits, 1, dividend, divisor))
            
        return output
            
       
sol = Solution()
print(sol.calcEquation(
    equations= [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],
    values= [3.0,0.5,3.4,5.6],
    queries=[["x2","x4"]]))

# print(sol.calcEquation(equations = [["a","b"],["b","c"]], 
#                  values = [2.0,3.0], 
#                  queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
#                  ))
# print(sol.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], 
#                        values = [1.5,2.5,5.0], 
#                        queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))

# print(sol.calcEquation(equations = [["a","b"]], 
#                        values = [0.5], 
#                        queries = [["a","b"],["b","a"],["a","c"],["x","y"]]))

# print(sol.calcEquation(
#     equations= [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],
#     values= [3.0,0.5,3.4,5.6],
#     queries=[["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]))


