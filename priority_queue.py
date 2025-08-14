import heapq

pq = []

heapq.heappush(pq, 10)
heapq.heappush(pq,5)
heapq.heappush(pq,2)

print(pq[0])

heapq.heappop(pq)

print(pq)