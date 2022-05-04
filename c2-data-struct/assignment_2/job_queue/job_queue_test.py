from heapq import *

pq = []  # priority queue
workers = [[0, 0], [0, 1], [0, 2]]
for worker in workers:
    heappush(pq, worker)

print(pq)

worker = heappop(pq)
print(worker[0], worker[1])
worker[0] += 2
heappush(pq, worker)
print(pq)
worker = heappop(pq)
print(worker[0], worker[1])
worker = heappop(pq)
print(worker[0], worker[1])
worker = heappop(pq)
print(worker[0], worker[1])
worker = heappop(pq)
print(worker[0], worker[1])