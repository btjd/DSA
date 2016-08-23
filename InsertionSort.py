from random import shuffle

def insertion_sort(sequence):
    """
    Insertion sort always maintains a sorted sublist in the lower
     positions of the list. Each new item is then inserted back
     into the previous sublist such that the sorted sublist
     is one item larger.
    """
    for i in range(1, len(sequence)):
        curr_val, curr_index = sequence[i], i
        while curr_index > 0 and sequence[curr_index-1]>curr_val:
            # We keep shifting bigger elements in the sublist to the right...
            sequence[curr_index] = sequence[curr_index-1]
            curr_index -= 1
        # ...then we insert our current value so that the next element in the sublist is smaller
        sequence[curr_index] = curr_val

### Let's do a test ###
def test_selection_sort():
    alist = [i for i in range(100)]
    shuffle(alist)
    insertion_sort(alist)
    assert alist == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                     11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                     21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                     31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                     41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                     51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                     61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
                     71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                     81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
                     91, 92, 93, 94, 95, 96, 97, 98, 99]