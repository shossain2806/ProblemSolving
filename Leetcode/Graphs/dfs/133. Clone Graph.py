from collections import deque
from lib2to3.pytree import Node
import queue

class Solution:
 
    def cloneGraph(self, node: 'Node') -> 'Node':
       
       if not node:
           return node
       
       visited = {}
       visited[node] = Node(node.val, [])
       queue = deque([node])
       
       while queue:
           curr_node = queue.popleft()
           
           for neighbor in curr_node.neighbor:
               if neighbor not in visited:
                   visited[neighbor] = Node(neighbor.val, [])
                   queue.append(neighbor)
                   
                visited[curr_node].neighbors.append(visited[neighbor])
                
        
        return visited[node]