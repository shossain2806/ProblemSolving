from collections import defaultdict
from email.policy import default
from pickle import FALSE, TRUE


def dfs(graph, visit, source, dest):
    flag = False
    if source == dest:
        return True
    neightbours = graph[source]
    if dest in neightbours:
        return True
    visit.add(source)
    for neightbour in neightbours:
        if neightbour in visit:
            continue
        flag = dfs(graph, visit, neightbour, dest)
        if flag == True:
            break
    return flag
    
    
graph = defaultdict(list)
edges = [["A", "B"], ["A", "C"], ["A", "D"], ["B", "E"], ["B", "F"], ["E", "F"], ["D", "E"], ["C", "E"]]    
for edge in edges:
    source = edge[0]
    dest = edge[1]
    graph[source].append(dest)
    graph[dest].append(source)

source = "A"
dest = "D"

visit = set()
print(dfs(graph, visit, source, dest))