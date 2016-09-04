def num_permus(str1, str2):
    """
    :param str1:
    :param str2:
    :return: count of permutations of str1 within str2
    """
    s = ''.join(sorted(str1))
    print s
    l = len(str1)
    count = 0
    for i in range(len(str2)):
        tmp = str2[i:i+l]
        print tmp + " | " + ''.join(sorted(tmp))
        if s == ''.join(sorted(tmp)):
            count += 1
    return count

str1 = 'cdba'
str2 = 'fgcbacbdaksbadcdldabhcbadop'

print num_permus(str1, str2)