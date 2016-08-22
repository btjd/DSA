def binary_iterative(sequence, item):
    found = False
    start = 0
    end = len(sequence)-1
    while start <= end and not found:
        mid = (start + end)/2
        if sequence[mid] == item:
            found = True
        else:
            if item < sequence[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return found

def binary_recursive(sequence, item):
    if len(sequence) == 0:
        return False
    else:
        mid = len(sequence)/2
        if sequence[mid] == item:
            return True
        else:
            if sequence[mid] < item:
                return binary_recursive(sequence[mid+1:], item)
            else:
                return binary_recursive(sequence[:mid], item)

print binary_recursive([1, 2, 4, 5, 6, 7, 8, 9, 10], 5)

### Let's run some tests ###

def test_binary_iterative():
    sequence = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    item = 3
    res = binary_iterative(sequence, item)
    assert res == False
    item = 8
    res = binary_iterative(sequence, item)
    assert res == True
    sequence = [1, 2]
    item = 2
    res = binary_iterative(sequence, item)
    assert res == True

def test_binary_recursive():
    sequence = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    item = 3
    res = binary_recursive(sequence, item)
    assert res == False
    item = 8
    res = binary_recursive(sequence, item)
    assert res == True
    sequence = [1, 2]
    item = 2
    res = binary_recursive(sequence, item)
    assert res == True