class Stack():
    """A python implementation of the Stack data structure"""

    def __init__(self):
        """ initialize the Stack """
        self.stack = list()

    def push(self, item):
        """Push an item into the stack"""
        self.stack.append(item)

    def pop(self):
        """Pop method: Removes the element at the top of the stack"""
        self.stack.pop()

    def peek(self):
        """Peek method: returns the element at the top of the stack"""
        return self.stack[-1]

    def isEmpty(self):
        """isEmpty method: returns boolean of wether stack is empty or not"""
        return self.stack == []

    def size(self):
        """size method: returns the current size of the stack"""
        return len(self.stack)


import pytest

def test_isEmpty():
    s = Stack()
    s.push('a')
    assert s.isEmpty() == False
    s.pop()
    assert s.isEmpty() == True

def test_push():
    s = Stack()
    with pytest.raises(TypeError) as type_exc:
        s.push()
    assert 'push() takes exactly 2 arguments (1 given)' in str(type_exc.value)
    # positive test for push
    a = 'a'
    s.push(a)
    assert s.peek() == a

