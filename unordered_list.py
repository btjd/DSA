class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class UnorderedList(object):
    def __init__(self, node=None):
        self.head = node
        if node is not None:
            self.size = 1
        else:
            self.size = 0

    def add_node(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def remove(self, item):
        current_node = self.head
        next_node = current_node.next
        found = False
        while next_node is not None and not found:
            if next_node.data == item:
                current_node.next = next_node.next
                next_node.next = None
            else:
                next_node = next_node.next
                current_node.next = next_node

    

    