from random import shuffle

class MinHeap(object):
    """
    Min heap is a list where first element is 0.
    The heap order property is as follows:
    In a heap, for every node x with parent p,
    the key in p is smaller than or equal to the key in x
    We use a list to represent a binary heap where
    the left child of a parent (at position p) is the node
     that is found in position 2p in the list. Similarly,
     the right child of the parent is at position 2p+1 in the list.
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
        self.heap[1] = self.heap[self.current_size]
        self.current_size = self.current_size - 1
        self.heap.pop()
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
            if self.heap[i * 2 + 1] > self.heap[i * 2]:
                return i * 2
            else:
                return (i * 2) + 1

    def build_heap(self, arr):
        self.current_size = len(arr)
        i = len(arr)//2
        self.heap = [0] + arr[:]
        while i > 0:
            self._perc_down(i)
            print i, self.heap
            i = i - 1

alist = [9,6,5,2,3]
#shuffle(alist)
print "Before: ", alist
h = MinHeap()
h.build_heap(alist)
print "After: ", h.heap

print h.del_min()
print h.del_min()
print h.del_min()
print h.del_min()
print h.del_min()
