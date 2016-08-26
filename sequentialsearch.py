def sequential(sequence, item):
    i = 0
    found = False
    while i < len(sequence) and not found:
        if sequence[i] == item:
            found = True
        else:
            i += 1
    return found

### Let's write some tests

def test_sequential_search():
    sequence = list(range(1000))
    item = 999
    res = sequential(sequence, item)
    assert res == True