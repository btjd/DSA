class Node(object):
    """
    http://www.cs.uml.edu/~jlu1/doc/source/report/BinarySearchTree1.html
    """
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.right = right
        self.left = left

class BST(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, val):
        if self.root:
            current_node = self.root
            while current_node:
                if key == current_node.key:
                    print "equal"
                    return None
                elif key < current_node.key:
                    print "less than"
                    if current_node.left:
                        print "left", key, current_node.key
                        current_node = current_node.left
                    else:
                        print "new node"
                        current_node.left = Node(key, val, current_node)
                        self.size += 1
                else: # when key > current_node.key
                    print "greater than"
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(key, val, current_node)
                        self.size += 1
        else:
            self.root = Node(key, val)
            self.size += 1

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
        if key == current_node.key:
            return True
        if node is None:
            return False
        elif key < current_node.key:
            self._search_recursive(current_node.left, key)
        else:
            self._search_recursive(current_node.right, key)

    def __contains__(self, key):
        return self._search_recursive(self.root, key)


t = BST()
t.insert(4, 'd')
print t[4]
t.insert(5, 'e')
print t[5]
t.insert(6, 'f')
print t[6]
# t.insert(3, 'c')
# t.insert(2, 'b')
# print 6 in t
# print t[2]
