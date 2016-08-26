class BinaryTree(object):
    def __init__(self, init_data=None):
        self.key = init_data
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, item):
        if self.left_child == None:
            self.left_child = BinaryTree(item)
        else:
            new_tree = BinaryTree(item)
            new_tree.left_child = self.left_child
            self.left_child = new_tree

    def insert_right(self, item):
        if self.right_child== None:
            self.right_child = BinaryTree(item)
        else:
            new_tree = BinaryTree(item)
            new_tree.right_child = self.right_child
            self.right_child = new_tree

def inorder_traversal(tree):
    if tree:
        for node in inorder_traversal(tree.left_child): yield node
        yield tree.key
        for node in inorder_traversal(tree.right_child): yield node

def preorder_traversal(tree):
    if tree:
        yield tree.key
        for node in preorder_traversal(tree.left_child): yield node
        for node in preorder_traversal(tree.right_child): yield node

def postorder_traversal(tree):
    if tree:
        for node in postorder_traversal(tree.left_child): yield node
        for node in postorder_traversal(tree.right_child): yield node
        yield tree.key


### Let's do some testing ###
def test_buildTree():
    t = BinaryTree()
    t.key = 'A'
    t.insert_left('B')
    t.insert_right('C')
    t.left_child.insert_left('D')
    t.left_child.insert_right('E')
    t.right_child.insert_left('F')
    t.right_child.insert_right('G')
    # print "     input Tree     "
    # print "          A         "
    # print "      B        C    "
    # print "    D   E    F   G  "
    #
    # print "Inorder traversal:"
    # print list(inorder_traversal(t))
    # print "Preorder traversal:"
    # print list(preorder_traversal(t))
    # print "Postorder traversal:"
    # print list(postorder_traversal(t))

    assert t.key == 'A'
    assert t.right_child.key == 'C'
    assert t.left_child.right_child.key == 'E'
    assert t.right_child.left_child.key == 'F'
    assert list(inorder_traversal(t)) == ['D', 'B', 'E', 'A', 'F', 'C', 'G']
    assert list(preorder_traversal(t)) == ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    assert list(postorder_traversal(t)) == ['D', 'E', 'B', 'F', 'G', 'C', 'A']

# test_buildTree()
