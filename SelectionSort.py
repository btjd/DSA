from random import shuffle

def selection_sort(sequence):
    """
    The selection sort improves on the bubble sort
    by making only one exchange for every pass through
    the list. In order to do this, a selection sort
    looks for the largest value as it makes a pass and,
    after completing the pass, places it in the proper location.
    """
    length = len(sequence)-1
    while length > 0:
        max_position = 0
        for i in range(length+1):
            if sequence[i] >= sequence[max_position]:
                max_position = i
        sequence[length], sequence[max_position] = sequence[max_position], sequence[length]
        print sequence
        length -= 1

### Let's do a test ###
def test_selection_sort():
    alist = [i for i in range(100)]
    shuffle(alist)
    selection_sort(alist)
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
