"""
General approach is to use a linear search converging two pointers
starting from both ends until we findthe rotation pivot and we
switch to binary search. If we knew whether the list was rotated
right or left, we can optimize the algorithm by initially keeping
one of the pointers static and only moving the other to find the
pivot point, but since we move both. This is done in place so it's
O(1) in terms of space complexity. Time complexity is O(n + log n)
"""

def search_rotated(arr, item):
    found = False
    start = 0
    end = len(arr) - 1
    # If list is rotated and sorted then
    # last element is going to be smaller
    # than first
    if arr[0] > arr[-1]:
        # We start by scanning from both ends. This loops stops when either our item or pivot
        # point is found
        print "loop1"
        while start < end and arr[start] < arr[start+1] and arr[end] > arr[end-1] and not found:
            if arr[start] == item or arr[end] == item:
                found = True
            else:
                start += 1
                end -= 1
    # If we haven't found item and hit pivot point
    # or if the array is rotated by n = len(arr)
    # switch to binary search
    while start <= end and not found:
        print "loop2"
        mid = (start + end)//2
        if arr[mid] == item:
            found = True
        else:
            if item < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return found

alist = [15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print search_rotated(alist, 3)