class Node(object):
    """
    http://www.cs.uml.edu/~jlu1/doc/source/report/BinarySearchTree1.html
    """
    def __init__(self, key, val, parent=None, left=None, right=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.right = right
        self.left = left

    def __iter__(self):
        if self:
            if self.left:
                for node in self.left:
                    yield node
            yield self.key
            if self.right:
                for node in self.right:
                    yield node

class BST(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, val):
        if self.root is None:
            self.root = Node(key, val)
            self.size += 1
            return True

        current_node = self.root
        done = False
        while current_node and not done:
            if key == current_node.key:
                current_node.val = val
                print "The specified node has been updated"
                done = True
            elif key < current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Node(key, val, current_node)
                    self.size += 1
                    done = True
            else: # when key > current_node.key
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(key, val, current_node)
                    self.size += 1
                    done = True

    def __setitem__(self, key, val):
        self.insert(key, val)

    def _search_iterative(self, node, key):
        current_node = node
        while current_node:
            if key == current_node.key:
                return current_node.val
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def __getitem__(self, key):
        return self._search_iterative(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def __contains__(self, key):
        return self._search_recursive(self.root, key)

    def remove(self, node):
        # If Node to be removed has two children
        if node.left and node.right:
            # Find successor that will replace it (next-largest)
            successor = node.right
            while successor.left:
                successor = successor.left
            # Once we find a successor, we copy it's key.val contents
            node.key = successor.key
            node.val = successor.val
            # Then remove the successor. We recursively call the same
            # function which handles either case of two children, one
            # child or no children
            self.remove(successor)
        # The node only has a left child
        elif node.left:
            self.replace(node, node.left)
        # The node only has a right child
        elif node.right:
            self.replace(node, node.right)
        # The node is a leaf, so just cut it off
        else:
            self.replace(node, None)
        self.size -= 1

    def replace(self, node, new_node):
        # If the node we need to replace is root:
        if node == self.root:
            self.root = new_node
            return
        parent = node.parent
        if parent.left and parent.left == node:
            parent.left = new_node
        elif parent.right and parent.right == node:
            parent.right = new_node
        else:
            print "Invalid replacement"

    def __iter__(self):
        if self:
            return self.root.__iter__()



input_list = [5, 2, 9, 4, 7, 1, 6, 3, 8]
bst = BST()
for e in input_list:
    bst.insert(e, 'A')

for node in bst: print node
print 9 in bst
print 10 in bst
print bst[2]