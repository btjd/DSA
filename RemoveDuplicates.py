def rem_dups(arr):
    for i in range(len(arr)-2, -1, -1):
        if arr[i] == arr[i+1]:
            arr.pop(i+1)
    return arr

arr = [1, 2, 3, 3, 4, 5, 6, 7, 7, 7, 7, 8, 9, 9]
print "Final: ", rem_dups(arr)