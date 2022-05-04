# python3
import os


class HeapBuilder:

    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]

        # Test case 04
        # with open('./tests/04') as f:
        #     n = int(f.readline())
        #     self._data = [int(s) for s in f.read().split()]

        assert n == len(self._data)
        self._size = n

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwapsNaive(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    self._data[i], self._data[j] = self._data[j], self._data[i]

    def sift_up(self, i):
        parent = i-1//2
        while i > 0 and self._data[parent] > self._data[i]:
            self._swaps.append((parent, i))
            self._data[i], \
                self._data[parent] = self._data[parent], self._data[i]
            i = parent

    def sift_down(self, i):
        min_index = i
        left_child = 2*i + 1
        right_child = 2*i + 2
        while i < self._size:
            if left_child < self._size and \
                    self._data[left_child] < self._data[min_index]:
                min_index = left_child
            if right_child < self._size and \
                    self._data[right_child] < self._data[min_index]:
                min_index = right_child
            if i != min_index:
                self._swaps.append((i, min_index))
                self._data[i], self._data[min_index] = \
                    self._data[min_index], self._data[i]
                i = min_index
                left_child = 2*i + 1
                right_child = 2*i + 2
            else:
                break

    def GenerateSwaps(self):
        for i in reversed(range(self._size//2)):
            self.sift_down(i)

    def Solve(self):
        self.ReadData()
        # self.GenerateSwapsNaive()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

    # print(heap_builder._data)
    # print(heap_builder._swaps)
