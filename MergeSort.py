from random import shuffle

def merge_sort(sequence):
    print ">> 1. sequence ", sequence
    res = []
    if len(sequence) < 2:
        return sequence
    mid = len(sequence)//2
    left_half = merge_sort(sequence[:mid])
    right_half = merge_sort(sequence[mid:])
    l = 0
    r = 0
    while l < len(left_half) and r < len(right_half):
        if left_half[l] > right_half[r]:
            res.append(right_half[r])
            print "2-1. Adding %d to res from right instead of %d from left" % (right_half[r], right_half[r])
            r += 1
        else:
            res.append(left_half[l])
            print "2-2. Adding %d to res from left instead of %d from right" % (left_half[l], right_half[r])
            l += 1
    # If we exhaust one of the sublists, just add the rest of what remains
    print "3. res is: ", res
    print "3. Left half: ", left_half[l:]
    res += left_half[l:]
    print "3. Right half: ", right_half[r:]
    res += right_half[r:]
    return res

alist = [7, 8, 6, 4, 1, 5, 3, 0, 9, 2]
res = merge_sort(alist)
print res

### Let's do a test ###
# def test_selection_sort():
#     alist = [i for i in range(100)]
#     shuffle(alist)
#     res = merge_sort(alist)
#     assert res == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#                     11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#                     21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#                     31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#                     41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
#                     51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
#                     61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
#                     71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
#                     81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
#                     91, 92, 93, 94, 95, 96, 97, 98, 99]


