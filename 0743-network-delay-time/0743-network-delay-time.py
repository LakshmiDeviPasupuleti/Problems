import heapq
class Solution:
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n + 1)]

        # Create graph
        for u, v, w in times:
            graph[u].append((v, w))

        # Distance from k to every node
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # (time, node)
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            if time > dist[node]:
                continue

            for nei, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))

        # If any node is unreachable
        if float('inf') in dist[1:]:
            return -1

        return max(dist[1:])