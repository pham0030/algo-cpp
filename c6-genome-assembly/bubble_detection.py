# python3
import sys
import itertools

class deBruijnGraph:

  def __init__(self, k, t, reads):
    self.k = k
    self.threshold = t
    self.graph = {}
    self.paths = {}
    self.bubbles = 0
    self.incoming = lambda vertex: self.graph[vertex][1] > 1
    self.outgoing = lambda vertex: len(self.graph[vertex][0]) > 1
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

  def count_bubbles(self):
    for k, v in self.graph.items():
      if self.outgoing(k):
        self.depth_first_search(path=[k], start=k, current=k, depth=0)
    for _, candidates_list in self.paths.items():
      for pair in itertools.combinations(candidates_list, r=2):
        if self.check_paths_disjoint(pair):
          self.bubbles += 1
    return self.bubbles

  def check_paths_disjoint(self, pair):
    return len(set(pair[0]) & set(pair[1])) == 2 
  def depth_first_search(self, path, start, current, depth):
    if current != start and self.incoming(current):
      self.paths.setdefault((start, current), list()).append(path[:])

    if depth == self.threshold:
      return

    for next_ in self.graph[current][0]:
      if next_ not in path:
        path.append(next_)
        self.depth_first_search(path, start, next_, depth + 1)
        path.remove(next_)


if __name__ == "__main__":
  data = sys.stdin.read().split()
  k, t, reads = data[0], data[1], data[2:]
  print(deBruijnGraph(int(k), int(t), reads).count_bubbles())