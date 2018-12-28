import random

def quicksort_1(arr):
    """
    quicksort using list comprehension
    """
    if not arr:
        return []

    return quicksort_1([x for x in arr if x < arr[0]]) \
        + [x for x in arr if x == arr[0]] \
        + quicksort_1([x for x in arr if x > arr[0]])

def qsort_compact(l):
    _qsort(l, 0, len(l)-1)

def _qsort_compact(l, fst, lst):
    if fst >= lst: return

    i, j = fst, lst
    pivot = l[random.randint(fst, lst)]

    while i <= j:
        while l[i] < pivot: i += 1
        while l[j] > pivot: j -= 1
        if i <= j:
            l[i], l[j] = l[j], l[i]
            i, j = i + 1, j - 1
    _qsort_compact(l, fst, j)
    _qsort_compact(l, i, lst)

def quicksort(array):
    """
    quicksort in-place implementation
    """
    _quicksort(array, 0, len(array) - 1)

def _quicksort(array, start, stop):
    # only proceed if our input array is of valid size
    if start < stop:
        # Set our pivot to be the first element of the array by default
        # then set our left marker to be at the start of the array and
        # right marker to be at the end of the array
        pivot, left, right = array[start], start, stop
        # Outer loop: while the left and right markers haven't converged
        while left <= right:
            # As long as our left marker is smaller than our pivot value
            # keep shifting to the left
            while array[left] < pivot:
                left += 1
            # As long as our right marker is larger than our pivot value
            # keep shifting to the right
            while array[right] > pivot:
                right -= 1
            # Once we get to a point where satisfy both conditions that
            # left marker is stopped at a value greater than pivot and
            # right marker is stopped at a value smaller than our pivot
            # swap both elements, increment both markers for next
            # outer loop iteration.
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        # Repeat the algorithm recursively for both left and right subsets
        # of our initial array. Outer while loop only stops when left > right
        # that's why we recurse on start/right and left/stop instead of
        # start/left and right/stop
        _quicksort(array, start, right)
        _quicksort(array, left, stop)


alist = [7, 8, 6, 4, 1, 5, 3, 0, 9, 2]
res = quicksort_1(alist)
print res
quicksort(alist)
print alist