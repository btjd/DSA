class Stack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        self.stack.pop()
        
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        if self.stack:
            return False
        else:
            return True
        
    def size(self):
        return len(self.stack)
    
    
if __name__ == '__main__':
    stack = Stack()
    stack.push('a')
    stack.push('b')
    print stack.peek()
    print stack.size()
    stack.pop()
    print stack.is_empty()
        
    
    
