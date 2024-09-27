from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    
        graph = defaultdict(list)

        # Build the graph
        for u, v, w in flights:
            graph[u].append([v, w])
        
        # Min-heap (priority queue) where elements are [cost, stops, node]
        dq = []
        heapq.heappush(dq, [0, 0, src])  # [cost, stops, node]

        # Track the best cost to each node with at most `k` stops
        distance = [[float('inf')] * (k + 2) for _ in range(n)]
        distance[src][0] = 0  # 0 cost to reach source with 0 stops

        while dq:
            cost, stops, node = heapq.heappop(dq)

            # If we reach the destination, return the cost
            if node == dst:
                return cost

            # If we have more stops than allowed, skip
            if stops > k:
                continue
            
            # Explore neighbors
            for nei, price in graph[node]:
                next_cost = cost + price
                if next_cost < distance[nei][stops + 1]:  # Only push if the new cost is better
                    distance[nei][stops + 1] = next_cost
                    heapq.heappush(dq, [next_cost, stops + 1, nei])

        # If no valid path was found, return -1
        return -1
#Dijikstra, but with stops you need a distance (cost) array with the cost to reach a place with each of k stops (k+2)
