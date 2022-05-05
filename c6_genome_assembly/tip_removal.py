# python3

import sys
import itertools

class deBruijnGraph:

  def __init__(self, k, reads):
    self.k = k
    self.threshold = self.k
    self.graph = {}
    self.paths = {}
    self.edges_pruned = 0
    self.construct_graph(self.construct_kmers(reads))

  def construct_kmers(self, reads):
    break_read_func = lambda read: [ read[j:j + self.k] for j in range(len(read) - self.k + 1) ]
    return [ kmer for read in reads for kmer in break_read_func(read) ]

  def construct_graph(self, kmers):
    def add_edge(graph, left, right):
      graph.setdefault(left, [set(), 0])
      graph.setdefault(right, [set(), 0])
      if right not in graph[left][0]:
        graph[left][0].add(right)
        graph[right][1] += 1
    for kmer in kmers:
      left, right = kmer[:-1], kmer[1:]
      if left != right:
        add_edge(self.graph, left, right)

  def count_incoming(self, v):
    return self.graph[v][1]

  def count_outgoing(self, v):
    return len(self.graph[v][0])
    
  def remove_outgoing(self, current, depth):
    if self.count_outgoing(current) > 1 or self.count_incoming(current) > 1:
      return False
    if depth == self.threshold:
      return False
    if self.count_outgoing(current) == 0:
      return True
    if self.remove_outgoing(next(iter(self.graph[current][0])), depth + 1):
      self.graph[current][0].pop()
      self.edges_pruned += 1
      return True
    return False

  def remove_incoming(self, current, depth):
    if depth == self.threshold:
      return False
    if self.count_outgoing(current) == 0 or self.count_incoming(current) > 1:
      return True
    if self.remove_incoming(next(iter(self.graph[current][0])), depth + 1):
      self.graph[current][0].pop()
      self.edges_pruned += 1
      return True
    return False


  def prune_tips(self):
    for k, v in self.graph.items():
      function_for_remove = None
      if len(v[0]) == 1 and v[1] == 0:
        function_for_remove = self.remove_incoming
      elif len(v[0]) > 1:
        function_for_remove = self.remove_outgoing
      else : continue

      condition = True
      while condition:
        condition = False
        for edge in v[0]:
          if function_for_remove(edge, 0):
            v[0].remove(edge)
            self.edges_pruned += 1
            condition = True
            break

    return self.edges_pruned

if __name__ == "__main__":
  k, reads = 15, sys.stdin.read().split()
  print(deBruijnGraph(k, reads).prune_tips())