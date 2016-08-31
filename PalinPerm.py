def palin_perm(string):
    """
    Given a string, write a functionto check if it is a
    permutation of a palidrome.
    """
    # Sort input string in an increasing, case-insensitive manner into a list
    sorted_input = sorted(string, key=str.lower)
    # remove spaces
    for s in string:
        if s == ' ':
            sorted_input.pop(sorted_input.index(s))
    # Working backwards, check that every pair is the same letter
    # either by direct comparison or bi difference of the ordinance.
    # The difference between the lower and upper case versions of the
    # same letter is always 32
    count = 0
    i = len(sorted_input)-1
    while i > 1:
        print i
        if sorted_input[i] == sorted_input[i-1] or abs(ord(sorted_input[i]) - ord(sorted_input[i-1])) == 32:
            i = i - 2
        else:
            i = i - 1
            count = count + 1
    # In case of a string of odd length, we will have no more than one
    # letter that is not repeated
    if count > 1:
        return False
    else:
        return True




print palin_perm("Tact Coa")

