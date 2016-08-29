class Node:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def has_left(self):
        return self.left

    def has_right(self):
        return self.right

    def is_left(self):
        return self.parent and self.parent.left == self

    def is_right(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right or self.left)

    def has_either_child(self):
        return self.right or self.left

    def has_both_children(self):
        return self.right and self.left

    def update_node(self, key, value, lc, rc):
        self.key = key
        self.val = value
        self.left = lc
        self.right = rc
        if self.has_left():
            self.left.parent = self
        if self.has_right():
            self.right.parent = self

    def __iter__(self):
        if self:
            # inorder traversal
            if self.left:
                for node in self.left:
                    yield node
            yield self.key
            if self.right:
                for node in self.right:
                    yield node

class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._recursive_put(key, val, self.root)
        else:
            self.root = Node(key, val)
        self.size = self.size + 1

    def _recursive_put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.has_left():
                   self._recursive_put(key, val, currentNode.left)
            else:
                   currentNode.left = Node(key, val, parent=currentNode)
        else:
            if currentNode.has_right():
                   self._recursive_put(key, val, currentNode.right)
            else:
                   currentNode.right = Node(key, val, parent=currentNode)

    def __setitem__(self, k, v):
       self.put(k, v)

    def get(self, key):
       if self.root:
           res = self._recursive_get(key, self.root)
           if res:
                  return res.val
           else:
                  return None
       else:
           return None

    def _recursive_get(self, key, currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._recursive_get(key, currentNode.left)
       else:
           return self._recursive_get(key, currentNode.right)

    def __getitem__(self, key):
       return self.get(key)

    def __contains__(self, key):
       if self._recursive_get(key, self.root):
           return True
       else:
           return False

    def delete(self, key):
      if self.size > 1:
         nodeToRemove = self._recursive_get(key, self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('key not in tree')

    def __delitem__(self, key):
       self.delete(key)

    def splice(self):
       if self.is_leaf():
           if self.is_left():
                  self.parent.left = None
           else:
                  self.parent.right = None
       elif self.has_either_child():
           if self.has_left():
                  if self.is_left():
                     self.parent.left = self.left
                  else:
                     self.parent.right = self.left
                  self.left.parent = self.parent
           else:
                  if self.is_left():
                     self.parent.left = self.right
                  else:
                     self.parent.right = self.right
                  self.right.parent = self.parent

    def find_successor(self):
      succ = None
      if self.has_right():
          succ = self.right.get_min()
      else:
          if self.parent:
                 if self.is_left():
                     succ = self.parent
                 else:
                     self.parent.right = None
                     succ = self.parent.find_successor()
                     self.parent.right = self
      return succ

    def get_min(self):
      current = self
      while current.has_left():
          current = current.left
      return current

    def remove(self, currentNode):
        # Node to be deleted is leaf
        # Just remove reference between node to be deleted 
        # and his parent
         if currentNode.is_leaf():
           if currentNode == currentNode.parent.left:
               currentNode.parent.left = None
           else:
               currentNode.parent.right = None
        # Node to be deleted has both children
        # If node has both children, find a replacement, this will be
        # the next-largest key in that node's tree. i.e, the smallest
        # of the bigger keys, or left-most child of the right subtree
        # (go right once then keep going left until you get to the 
        # smallest node) that last node will have one child at the most. 
         elif currentNode.has_both_children():
           succ = currentNode.find_successor()
           succ.splice()
           currentNode.key = succ.key
           currentNode.val = succ.val
           # Node to be deleted has one child
           # Just rearrange pointers to make parent and child
           # of node to be deleted to point to each other. We will
           # deal with six cases:
           # 1. Node to be deleted has a left child and is a left child
           # 2. Node to be deleted has a left child and is a right child
           # 3. Node to be deleted has a left child and is root.
           # 4. Node to be deleted has a right child and is a left child
           # 5. Node to be deleted has a right child and is a right child
           # 6. Node to be deleted has a right child and is root.
         else:
           if currentNode.has_left():
             if currentNode.is_left():
                 currentNode.left.parent = currentNode.parent
                 currentNode.parent.left = currentNode.left
             elif currentNode.is_right():
                 currentNode.left.parent = currentNode.parent
                 currentNode.parent.right = currentNode.left
             else:
                 currentNode.update_node(currentNode.left.key, 
                                    currentNode.left.val, 
                                    currentNode.left.left, 
                                    currentNode.left.right)
           else:
             if currentNode.is_left():
                 currentNode.right.parent = currentNode.parent
                 currentNode.parent.left = currentNode.right
             elif currentNode.is_right():
                 currentNode.right.parent = currentNode.parent
                 currentNode.parent.right = currentNode.right
             else:
                 currentNode.update_node(currentNode.right.key, 
                                    currentNode.right.val, 
                                    currentNode.right.left, 
                                    currentNode.right.right)

mytree = BST()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"
for node in mytree.root: print node
print(mytree[6])
print(mytree[2])