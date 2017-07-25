class Node(object):
    def __init__(self, d):
        self.data = d
        self.next = None
    
class UnorderedList(self):
    def __init__(self):
        self.head = None
        self.count = 0
        
    def is_empty(self):
        return self.head == None
    
    def add_node(self, NewNode):
        temp = Node(NewNode)
        temp.next = self.head
        self.head = temp
        self.count += 1
        
    def size(self):
        return self.size
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return count
    
    def delete_node(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
                
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next
            
        self.count -= 1