from random import shuffle

class MinHeap(object):
    """
    Min heap is a list where forst element is 0. at every element location p
    the children are always at 2p and 2p+1. Min value is always at the top or
    index 1 of our heap list
    """
    def __init__(self):
        self.heap = [0]
        self.current_size = 0

    def insert(self, node):
        # Insert new element at the bottom of the tree or end of the list
        self.heap.append(node)
        self.current_size = self.current_size + 1
        # We perc up to satisfy the property that a parent node is always
        # smaller than the children
        self._perc_up(self.current_size)

    def _perc_up(self, i):
        # While parent of current node is not at the top of the heap
        while i // 2 > 0:
            # If our current node, the child is smaller than its parent,
            # swap their locations
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            # Go up one level
            i = i // 2

    def del_min(self):
        # Min val is always at the top of the tree, at index 1
        min_val = self.heap[1]
        # Replace the min val at index 1 with the last item of heap
        self.heap[1] = self.heap.pop()
        self.current_size = self.current_size - 1
        # perc down to restore balance
        self._perc_down(1)
        return min_val

    def _perc_down(self, i):
        # while we haven't reached the last leaf
        while (i * 2) < self.current_size:
            # Figure out which one of the two children is smaller
            mc = self._min_child(i)
            # swap positions with them
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            # current position is where min child was
            i = mc

    def _min_child(self, i):
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            if (i * 2) + 1 > i * 2:
                return i * 2
            else:
                return (i * 2) + 1

    def build_heap(self, arr):
        self.current_size = len(arr)
        i = len(arr)//2
        self.heap = [0] + arr[:]
        while i > 0:
            self._perc_down(i)
            i = i - 1

alist = range(1, 10)
shuffle(alist)
print "Before: ", alist
h = MinHeap()
h.build_heap(alist)
print "After: ", h.heap