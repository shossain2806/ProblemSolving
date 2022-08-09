from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticker_count = len(tickets) 
        adjacency_matrix = [[] for _ in range(ticker_count - 1)]
        
        for ticket in tickets:
            adjacency_matrix[ticket[0]].append(ticket[1])
        
        stack = ["JFK"]
        visited = set()
        path = { }
        while(stack):
            current_node = stack.pop()
            
            for neightbour in adjacency_matrix[current_node]:
                stack.append(neightbour)
                path[neightbour].append(current_node)    
            
        print(path)
        
        
        
sol = Solution()
sol.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])