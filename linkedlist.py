class Node(object):
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def search(self, item):
        current = self.head
        while current.next != None:
            if current.data == item:
                return True
            else:
                current = current.next
        return False

    def remove(self, item):
        if self.search(item) is False:
            print " Specified Node does not exist in the list"
        else:
            current = self.head
            previous = None
            found = False
            while current != None and not found:
                if current.data != item:
                    previous = current
                    current = current.next
                else:
                    found = True
            if current == self.head:
                self.head = current.next
            else:
                previous.next = current.next

    def show(self):
        current = self.head
        result = str()
        while current != None:
            result += (str(current.data) + " -> ")
            current = current.next
        result += 'None'
        return result


# Let's do some testting

def test_linked_list():
    l = LinkedList()
    l.add('a')
    l.add('b')
    l.add('c')
    assert l.show() == "c -> b -> a -> None"
    l.remove('b')
    assert l.show() == "c -> a -> None"
    assert l.search('x') == False