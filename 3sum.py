def three_sum(arr):
    """
    :param arr:
    :return: True if three elements within the array sum up to 0
    """
    pos = [x for x in arr if x > 0]
    print pos
    neg = [abs(x) for x in arr if x < 0]
    print neg
    found = False
    i = 0
    while i < len(pos) - 1 and not found:
        print "Current positive is: ", pos[i]
        tmp = [x for x in neg if x < pos[i]]
        print tmp
        tmp.sort()
        start = 0
        end = len(tmp)-1
        while end >= start and not found:
            print start, end
            if tmp[start] + tmp[end] == pos[i]:
                print "Ding!"
                found = True
            elif tmp[start] + tmp[end] > pos[i]:
                end = end - 1
            elif tmp[start] + tmp[end] < pos[i]:
                start = start + 1
    return found

arr = [4, 3, -1, 2, -2, 10]
print three_sum(arr)