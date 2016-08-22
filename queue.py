class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

### Let's do some testing ###

def test_queue():
    q = Queue()
    q.enqueue('a')
    q.enqueue('b')
    assert q.isEmpty() == False
    assert q.dequeue() == 'a'
    assert q.size() == 1