def rem_intervals(intervals, start, end):
    """
    :param intervals:
    :param start:
    :param end:
    :return: A subste of intervals where sub-intervals in the start/end range are removed
    Example : Inputs : [[1,2], [2,3], [3,4]] and 2,3 ; Outpus : [[1,2], [2,4]]
    """
    i = 0
    while i < len(intervals)-1:
        print "Current index is: ", i, intervals[i]
        if intervals[i][0] >= start and intervals[i][1] <= end:
            print "Removing interval: ", intervals[i]
            intervals.pop(i)
        elif intervals[i][0] == end:
            intervals[i][0] = start
            i = i + 1
        else:
            i = i + 1
    return intervals


intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
start = 2
end = 5
print rem_intervals(intervals, start, end)